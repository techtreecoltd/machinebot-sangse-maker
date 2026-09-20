# S8 / 1.16.5 검증

추상적인 제품 가치를 사진만으로 전달하기 어려운 경우를 판별하는 CG 시각화 카탈로그를 추가했다. 범용 이미지 분기를 늘리지 않고 기존 연출·효용·상세 흐름에 공통 판단을 연결했다.

## 설계 반영

- `references/cg-visualization-catalog.md`: 차단·보호·흐름, 재질·표면, 사용·신체 접촉, 부위·해부학적 관심, 구조·메커니즘의 다섯 유형과 근거별 허용 범위를 정의했다.
- `machinebot-lifestyle/SKILL.md`: 연출컷도 일반 사진으로 보이지 않는 가치가 있으면 CG 후보를 만들고, 근거 없는 기능·의학적 의미를 차단하도록 연결했다.
- `machinebot-benefit-visual/SKILL.md`: 추상 효과가 필요한 경우 카탈로그를 읽되, 근거가 없으면 관심 부위·표면 관찰·구조 설명 수준으로 낮추도록 연결했다.
- `sales-visual-strategy.md`, `validation/behavior-evaluation.md`: 공통 소구 설계와 S8 시나리오에 CG 판단을 추가했다.
- README와 플러그인 README: 제품 가치가 보이지 않는 개념을 CG로 판단해 연출·효용·상세에 연결하는 동작을 설명했다.

## 검증

- `scripts/package_plugin.py 1.16.5`: PASS. 6개 스킬, 34개 파일, 링크·버전·CRC·바이트 일치와 SHA-256을 확인했다. ZIP SHA-256은 `e0c9baa63756e046c46e14b5a1a53eeb215b4849442797d7e8493ac05bb9e24b`이며 `.sha256` 기록과 일치한다. [패키지 기록](package-1.16.5.json)
- 원본 `quick_validate.py`·`validate_plugin.py`: PASS.
- `validation/package-check-1.16.5` 압축 해제본 `quick_validate.py`·`validate_plugin.py`: PASS.
- `python -m unittest validation/test_product_context.py validation/test_package_validation.py`: PASS, 10개.
- 기존 합성 트레이 결과 `benefit-01`의 칸별 구조 설명, `benefit-02`의 열린 상부·손 동작, `benefit-03`의 T 접점 확대는 직접 열람한 안전한 CG형 구조 시각화 사례로 유지한다.
- 별도 synthetic fixture에서 `output/harness-demo-20260921/cg-catalog-demo/`의 세 유형을 실제 생성·열람했다. `cg-01-uv-concept.png`는 차단 개념, `cg-02-material-surface.png`는 직조 표면과 확대 인셋, `cg-03-lumbar-interest-zone-final.png`는 사용 장면과 허리 관심 부위 실루엣을 보여준다. 첫 허리 시도 `cg-03-lumbar-interest-zone.png`는 빨간 발광이 효과처럼 읽힐 수 있어 FAIL로 기록하고 재사용하지 않았다. 해시·검수는 `cg-demo-record.json`과 `review.md`에 남겼다.

## 판단 예시

- 자외선 차단 시험이 있으면 시험 대상·조건 안에서 광선 차단 개념을 보여주고, 없으면 햇빛 아래 사용 장면만 만든다.
- 재질 문서가 있으면 표면 구조 접사를 만들고, 없으면 `표면 질감 연출`까지만 허용한다.
- 척추 제품은 실제 접촉 자세와 관심 부위를 보여줄 수 있지만, 의료 근거 없이 빨간 영역을 통증 치료·교정·완화 결과로 설명하지 않는다.
- 모든 CG는 별도 레이어를 합성하지 않고 제품·장면·CG·카피를 한 호스트 호출에서 평탄화한다.

이 버전은 판단 체계와 연결 및 합성 fixture 검수를 완료한 것이며, 특정 제품의 자외선 차단·재질 성능·척추 효능을 검증한 결과가 아니다. 실제 제품 자료가 들어오면 해당 자료와 옵션에 맞춰 유형별 근거를 다시 닫아야 한다.
