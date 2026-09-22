# 제품 원본과 자산 인계

누끼나 다른 제작에서 계속 사용할 자료는 작업 폴더의 `product-context.json`에 저장한다. 같은 제품·옵션이면 같은 파일을 이어 쓴다. 제품마다 폴더를 분리하고 원본을 덮어쓰지 않는다. 파일 도구가 없으면 동일 구조를 대화/첨부로 전달하되 저장했다고 말하지 않는다. 기록 실패는 납품 보고에 표시한다.

## 최소 레코드

```json
{
  "schema_version": 1,
  "product": {"id": "example-blue", "name": "예시 제품", "variant": "blue", "mode": "real"},
  "sources": [{"id": "src-1", "path": "source/front.png", "sha256": "실제 64자리 SHA-256", "role": "product-original"}],
  "identity": {"locked": ["형상", "파랑", "원본 인쇄"], "unseen": ["뒷면"]},
  "facts": [{"id": "fact-1", "text": "사진에서 보이는 구조", "source_ids": ["src-1"], "basis": "observed"}],
  "unknowns": ["확인되지 않은 소재·성능"],
  "assets": [],
  "plans": []
}
```

예제 문자열은 실제 경로·해시·관찰로 바꾼다. mode는 real 또는 synthetic이다. 가상 테스트·콘셉트는 synthetic으로 끝까지 유지하며 실물 동일성 검증으로 승격하지 않는다. facts의 basis는 observed / supplied / documented / synthetic-spec 중 하나이며 모든 근거는 sources ID로 연결한다. 미확인 주장은 facts에 넣지 않는다. real 제품에 synthetic-spec을 사용할 수 없다.

각 자산은 다음 필드를 기록한다.

| 필드 | 내용 |
|---|---|
| id, kind, path, sha256 | 고유 ID, cutout/lifestyle/detail/thumbnail/benefit, 기록 기준 상대 파일 경로와 현재 해시 |
| source_ids, source_hashes | 실제 참조한 원본 IDs와 생성 당시 해시 스냅샷 |
| variant | product.variant와 같은 옵션 |
| status | unreviewed / pass / failed / stale |
| review | 검수 note, reviewer, 현재 파일을 직접 열어 확인한 viewed=true, 검수 대상 sha256; 미검수면 null |
| scene_id, appeal_ids | 장면과 소구 연결. 단순 누끼면 빈 배열 가능 |
| generation | 호스트 기능명, 실제 시도 수, 저장한 프롬프트 경로. 없는 호출 ID를 발명하지 않음 |

원본·제품 정보는 연출 스킬에 한 번만 전달하고, 파생 컷에 이상이 있으면 원본으로 돌아간다. 경로는 작업 폴더 안을 가리키고 사용자 원본은 필요하면 복사한다. 원본/자산을 열 수 없으면 해시만으로 pass를 유지하지 않는다.

## 재개·수정

1. 버전·제품·옵션을 확인하고 원본과 재사용할 자산의 존재·해시를 확인한다. 알 수 없는 schema_version은 조용히 변환하지 않는다.
2. 수정된 원본을 발견하면 해당 source_hashes를 가진 자산을 stale로 표시한다. 제품 옵션이 다르면 새 제품 기록을 만든다. 사실 변경은 영향받는 소구·카피·계획 승인을 재검토한다.
3. pass이면서 실제 파일·해시·원본·옵션이 맞는 자산만 재사용한다. failed/unreviewed/stale은 납품 완료나 후속 기준으로 사용하지 않는다.
4. 수정 파일은 새 이름/ID로 저장하고 직접 재검수한다. 이전 실패·시도·원본 연결을 삭제하지 않는다.
5. 파일 도구가 있으면 임시 파일 작성 → JSON 파싱 확인 → 같은 폴더의 기록 파일 교체로 갱신한다. 쓰기 실패 시 기존 기록을 보존한다.

선택적 읽기 전용 검사: `python <진입 스킬 경로>/scripts/validate_context.py <작업 폴더>/product-context.json`. 이 검사는 구조·파일·해시·인계를 확인할 뿐 시각 검수를 대신하지 않는다. Python이 없는 호스트에서는 위 항목을 가용 파일 도구로 확인하며 필수 런타임으로 설치를 요구하지 않는다.

썸네일은 메인 한 장도 plans.scope 또는 연결된 제작 기록에 구매 질문, 표현 선택/대안 이유, 자료별 역할과 실제 입력/제외, 정확 카피 또는 없음의 이유, 채널 확인 상태를 남긴다. 기존 schema_version 1을 유지하며 새 파일/필드를 필수 계약으로 강제하지 않는다. 실제 검수 note는 이 방향이 결과에 보이는지 설명한다.

plans에는 선택한 구성의 id, scope, status(proposed/approved/stale), approval_evidence, slots를 둔다. 슬롯은 id, kind, asset_id(null이면 미제작)이며 상세페이지는 마지막 슬롯 role=faq를 명시한다. 정확 수량과 문구·장면 계획은 scope에 보존한다. 실제 승인 전 approved나 승인 증거를 발명하지 않는다. 패키지 구성 승인에 상세 패널 구성도 포함됐다면 별도 승인을 반복하지 않는다.

FAQ는 [구매 결정형 FAQ](purchase-decision-faq.md)의 구매 장벽·질문/정확 답변·조건·근거 ID·새 판단 정보·스타일·미해결 사실을 plans.scope 또는 연결된 제작 기록에 남긴다. 부분 FAQ 요청은 전체 상세/패키지 계획과 구분해 그 한 슬롯만 기록한다. review.note는 구매 결정 도움·근거·정보 진전·위계·문자/모바일·규격의 실제 판정과 미검증 항목을 담는다. 기존 schema_version 1을 유지하며 구조 검사 통과를 의미/시각 검수 통과로 해석하지 않는다.
