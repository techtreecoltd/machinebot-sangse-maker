"""Read-only handoff integrity check; never grants visual approval or runs generation."""
import hashlib
import json
import re
import sys
from pathlib import Path

KINDS = {"cutout", "lifestyle", "detail", "thumbnail", "benefit"}


def validate(data, root):
    errors = []
    root = Path(root).resolve()

    def check(ok, message):
        if not ok:
            errors.append(message)

    def file_hash(item, label):
        path = item.get("path", "")
        digest = item.get("sha256", "")
        check(bool(re.fullmatch(r"[a-f0-9]{64}", digest)), f"{label}: invalid sha256")
        candidate = (root / path).resolve()
        if not path or not candidate.is_relative_to(root) or not candidate.is_file():
            errors.append(f"{label}: missing or outside-workspace file")
        elif hashlib.sha256(candidate.read_bytes()).hexdigest() != digest:
            errors.append(f"{label}: file changed")

    check(data.get("schema_version") == 1, "unsupported schema_version")
    product = data.get("product", {})
    check(all(product.get(k) for k in ("id", "name", "variant")), "product identity missing")
    check(product.get("mode") in {"real", "synthetic"}, "invalid product mode")
    identity = data.get("identity", {})
    check(bool(identity.get("locked")) and isinstance(identity.get("unseen"), list), "identity lock missing")
    sources = {}
    for source in data.get("sources", []):
        sid = source.get("id")
        check(bool(sid) and sid not in sources, "duplicate/missing source id")
        sources[sid] = source
        file_hash(source, str(sid))
    check(bool(sources), "no sources")
    facts = set()
    for fact in data.get("facts", []):
        fid = fact.get("id")
        check(bool(fid) and fid not in facts, "duplicate/missing fact id")
        facts.add(fid)
        check(bool(fact.get("text")), f"{fid}: empty fact")
        check(bool(fact.get("source_ids")) and set(fact["source_ids"]) <= sources.keys(), f"{fid}: missing evidence")
        check(fact.get("basis") in {"observed", "supplied", "documented", "synthetic-spec"}, f"{fid}: invalid basis")
        check(not (product.get("mode") == "real" and fact.get("basis") == "synthetic-spec"), f"{fid}: synthetic claim on real product")
    assets = {}
    for asset in data.get("assets", []):
        aid = asset.get("id")
        check(bool(aid) and aid not in assets, "duplicate/missing asset id")
        assets[aid] = asset
        file_hash(asset, str(aid))
        check(asset.get("kind") in KINDS, f"{aid}: invalid kind")
        check(asset.get("variant") == product.get("variant"), f"{aid}: variant mismatch")
        refs = asset.get("source_ids", [])
        check(bool(refs) and set(refs) <= sources.keys(), f"{aid}: missing source")
        for sid in refs:
            check(asset.get("source_hashes", {}).get(sid) == sources.get(sid, {}).get("sha256"), f"{aid}: stale source {sid}")
        check(asset.get("status") in {"unreviewed", "pass", "failed", "stale"}, f"{aid}: invalid status")
        if asset.get("status") == "pass":
            review = asset.get("review") or {}
            check(review.get("viewed") is True and bool(review.get("note")) and bool(review.get("reviewer")), f"{aid}: missing direct review")
            check(review.get("sha256") == asset.get("sha256"), f"{aid}: stale review")
    plans = set()
    for plan in data.get("plans", []):
        pid = plan.get("id")
        check(bool(pid) and pid not in plans, "duplicate/missing plan id")
        plans.add(pid)
        check(plan.get("status") in {"proposed", "approved", "stale"}, f"{pid}: invalid plan status")
        if plan.get("status") == "approved":
            check(bool(plan.get("approval_evidence")), f"{pid}: missing approval evidence")
        used, slots = set(), set()
        for slot in plan.get("slots", []):
            check(bool(slot.get("id")) and slot["id"] not in slots, f"{pid}: duplicate/missing slot")
            slots.add(slot.get("id"))
            aid = slot.get("asset_id")
            if aid is None:
                continue
            asset = assets.get(aid, {})
            check(aid not in used, f"{pid}: duplicate asset count")
            used.add(aid)
            if plan.get("status") == "approved":
                check(asset.get("status") == "pass", f"{pid}: unusable asset {aid}")
            check(asset.get("kind") == slot.get("kind"), f"{pid}: asset kind mismatch")
    return errors


if __name__ == "__main__":
    try:
        path = Path(sys.argv[1])
        result = validate(json.loads(path.read_text(encoding="utf-8-sig")), path.parent)
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        print(f"INVALID: {exc}")
        sys.exit(1)
    print("\n".join(result) if result else "PASS: record, files, hashes and handoff references; visual quality requires human/agent inspection")
    sys.exit(bool(result))
