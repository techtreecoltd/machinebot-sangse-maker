# S9 / 1.17.0 검증

> 미배포 후보의 과거 기록. 아래 네 장 PASS는 최종 판정이 아니다. 세트 재검토에서 1·3·4번의 각도 중복을 발견해 3·4번을 제외했다. 현재 결과는 [1.17.1 검증](release-1.17.1-validation.md)을 따른다. 1.17.0 ZIP은 당시 스냅샷이며 이후 변경한 소스와 일치하지 않는다.

누끼컷의 의미를 투명 PNG 추출물에서 흰색 스튜디오 제품 마스터컷으로 정정했다. 이 버전의 `cutout` 자산은 기존 패키지 연결과 호환되는 내부 종류 값이며, 실제 산출물 포맷은 불투명 흰색 배경 제품 사진이다.

## 구현 변경

- `machinebot-product-cutout/SKILL.md`: 정면·3/4·측면·상부 등 확인 가능한 다각도, 중성 화이트밸런스, 큰 확산광, 자연스러운 접지 그림자, 흰색 배경과 직접 시각 검수로 계약을 교체했다.
- `references/studio-product-shots.md`: 누끼컷의 사용자 의미와 생성·실패·검수 규칙을 단일 참고 문서로 기록했다.
- `branches.md`, `image-production.md`, `quality-gates.md`, intake·README·PRD·행동 검증을 새 의미에 맞게 동기화했다.
- `validate_studio_shots.py`: 이미지가 충분히 크고 불투명하며 네 모서리가 흰색 계열인지 읽기 전용으로 확인한다. 이 검사는 제품 정체성의 직접 시각 검수를 대체하지 않는다.

## 실제 fixture

합성 트레이 원본 `output/harness-demo-20260921/studio-cutout-v2/source/tray-reference.png`를 제품 기준으로 사용했다. 호스트 이미지 생성 편집으로 다음 네 장을 만들고 모두 직접 열람했다.

| 파일 | 구도 | 직접 검수 |
|---|---|---|
| `studio-01-front-three-quarter.png` | 정면 3/4 | PASS |
| `studio-02-front.png` | 정면 | PASS |
| `studio-03-left-three-quarter.png` | 좌측 3/4 | PASS |
| `studio-04-top-three-quarter.png` | 상부 3/4 | PASS |

네 장 모두 흰색 배경, 중성 조명, 부드러운 접지 그림자, 충분한 제품 여백, 세 칸 구조를 확인했다. 소품·카피·가짜 로고는 없다. 네 장은 1254 × 1254 RGB 이미지이며 기술 validator가 PASS했다. 해시와 직접 검수 기록은 `studio-shot-record.json`과 `review.md`에 남겼다.

## 경계

fixture는 합성 제품으로 구현 계약과 시각 검수 절차를 검증한다. 실제 판매 제품의 색상·재질·치수 동일성을 증명하지 않는다. 사용자가 투명 PNG를 별도로 요청하는 경우에는 기본 흰색 스튜디오 마스터컷과 구분된 추가 편집으로 기록한다.
