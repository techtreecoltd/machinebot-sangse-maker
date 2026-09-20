"""Validate an approved package plan against the shared product context."""
import argparse
import hashlib
import json
import sys
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("context", type=Path)
    ap.add_argument("--plan-id", required=True)
    args = ap.parse_args()
    context = args.context.resolve()
    data = json.loads(context.read_text(encoding="utf-8-sig"))
    plans = [p for p in data.get("plans", []) if p.get("id") == args.plan_id]
    if len(plans) != 1:
        print(f"FAIL: expected one plan {args.plan_id}, found {len(plans)}")
        return 1
    plan = plans[0]
    assets = {a.get("id"): a for a in data.get("assets", [])}
    sources = {s.get("id"): s for s in data.get("sources", [])}
    errors, seen, seen_slot_ids, seen_paths, counts, slots = [], set(), set(), set(), {}, []
    if plan.get("status") != "approved":
        errors.append(f"plan is not approved: {plan.get('status')}")
    for slot in plan.get("slots", []):
        sid, aid, kind = slot.get("id"), slot.get("asset_id"), slot.get("kind")
        if not sid or sid in seen_slot_ids:
            errors.append(f"duplicate or missing slot: {sid}")
        seen_slot_ids.add(sid)
        asset = assets.get(aid)
        slots.append({"slot_id": sid, "asset_id": aid, "kind": kind, "status": asset.get("status") if asset else "missing"})
        counts[kind] = counts.get(kind, 0) + 1
        if aid in seen:
            errors.append(f"duplicate asset in slots: {aid}")
        seen.add(aid)
        if not asset:
            errors.append(f"missing asset: {aid}")
            continue
        if asset.get("status") != "pass":
            errors.append(f"asset not pass: {aid} ({asset.get('status')})")
        if asset.get("kind") != kind:
            errors.append(f"kind mismatch: {aid}")
        if asset.get("variant") != data.get("product", {}).get("variant"):
            errors.append(f"variant mismatch: {aid}")
        asset_path = asset.get("path")
        if asset_path in seen_paths:
            errors.append(f"duplicate asset file in slots: {asset_path}")
        seen_paths.add(asset_path)
        review = asset.get("review") or {}
        if asset.get("status") == "pass" and (review.get("viewed") is not True or review.get("sha256") != asset.get("sha256")):
            errors.append(f"review/hash not closed: {aid}")
        for source_id in asset.get("source_ids", []):
            if source_id not in sources or asset.get("source_hashes", {}).get(source_id) != sources[source_id].get("sha256"):
                errors.append(f"stale source: {aid} -> {source_id}")
        path = (context.parent / asset.get("path", "")).resolve()
        if not path.is_file():
            errors.append(f"missing asset file: {aid}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != asset.get("sha256"):
            errors.append(f"asset hash changed: {aid}")
    tier = plan.get("scope", {}).get("tier")
    if tier == "lite":
        expected = {"cutout": (1, 2), "thumbnail": 6, "lifestyle": 4, "benefit": 3, "detail": 6}
    elif tier == "full":
        expected = {"cutout": (2, 4), "thumbnail": (6, 8), "lifestyle": (6, 10), "benefit": (3, 6), "detail": (8, 10)}
    else:
        errors.append(f"unsupported package tier: {tier}")
        expected = {}
    for kind, required in expected.items():
        if isinstance(required, tuple):
            if not required[0] <= counts.get(kind, 0) <= required[1]:
                errors.append(f"quantity outside full range: {kind}={counts.get(kind, 0)}")
        elif counts.get(kind, 0) != required:
            errors.append(f"quantity mismatch: {kind}={counts.get(kind, 0)}, expected {required}")
    report = {"plan_id": args.plan_id, "tier": plan.get("scope", {}).get("tier"), "counts": counts, "slot_count": len(slots), "complete": not errors, "errors": errors, "slots": slots}
    out = context.parent / "package-manifest.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("PASS: package slots, quantities, reviews, variants, source hashes and files" if not errors else "FAIL: " + "; ".join(errors))
    print(f"manifest: {out}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
