# S7 / 1.16.1 검증

전체 이미지 패키지 연결 계약과 부분 패키지 차단 검증을 추가했다. 전체 패키지는 독립 생성 스킬이 아니라 누끼·연출·효용·썸네일·상세페이지 결과를 슬롯으로 연결한다.

## 구현·구조 검증

- `scripts/package_plugin.py 1.16.1`: PASS. 6개 스킬, 33개 파일, 원본/압축 해제본 링크·버전·CRC·바이트 일치와 SHA-256을 확인했다. ZIP SHA-256은 `4c34500dc695f662ebe041e79552bac40c9a11c1fff76b26b60a58d55cf9c2fb`이며 `.sha256` 기록과 일치한다.
- 원본 `quick_validate.py`: PASS.
- 원본 `validate_plugin.py`: PASS.
- `validation/package-check-1.16.1/machinebot-ecommerce-studio`의 압축 해제본 `quick_validate.py`: PASS.
- 압축 해제본 `validate_plugin.py`: PASS.
- `python -m unittest validation/test_product_context.py validation/test_package_validation.py`: PASS, 7개.
- `validate_context.py output/harness-demo-20260921/product-context.json`: PASS. `proposed` 계획은 미완료 자산을 기록할 수 있고 `approved` 계획에서만 성공 자산을 강제하도록 경계를 보완했다.

## 실제 개발 패키지 연결

합성 테스트 제품 `demo-tray-blue`에 라이트 패키지 계획 `demo-package-lite`를 만들었다. 수량은 누끼 1, 연출 4, 효용 3, 썸네일 6, 상세 6이며 모두 독립 스킬의 서로 다른 asset ID를 연결했다. 상세 마지막 슬롯은 FAQ다.

| 종류 | 계획 수량 | pass 자산 | 상태 |
|---|---:|---:|---|
| 누끼 | 1 | 0 | 차단: `cutout-final` 색상 보존 실패 |
| 연출 | 4 | 4 | 직접 열람·해시 검수 PASS |
| 효용 | 3 | 3 | 직접 열람·해시 검수 PASS |
| 썸네일 | 6 | 6 | 직접 열람·해시 검수 PASS |
| 상세페이지 | 6 | 6 | 1080×2160, 마지막 FAQ, 직접 열람·해시 검수 PASS |

`validate_package.py ... --plan-id demo-package-lite`: **의도된 FAIL** — `plan is not approved: proposed; asset not pass: cutout-final (failed)`. 부분 manifest는 `output/harness-demo-20260921/package-manifest.json`에 기록했고 `complete: false`다. 누끼 색상 보존 문제가 해결되기 전에는 ZIP이나 고객 전달용 전체 패키지를 완료로 표시하지 않는다.

## 범위와 제한

직접 생성·검수한 이미지는 가상 트레이 테스트 픽스처다. 실제 판매 제품의 소재·치수·내구성·인증·성능을 증명하지 않는다. 누끼는 호스트 이미지 생성 재시도에서도 원본보다 청색이 증가해 failed로 유지했다. 제품 픽셀을 보존하는 코드 마스킹은 현재 AGENTS 제약과 사용자 미응답 결정 사항 때문에 실행하지 않았다.


