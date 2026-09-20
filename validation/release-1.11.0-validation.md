# S2 / 1.11.0 검증

2026-09-21. 범위: 독립 제품 누끼, 공통 제작 규칙과 제품별 원본·검수 자산 인계. 이미지 실행은 호스트 image_gen을 사용했다. 가상 제품이며 실물 재현 시험이 아니다.

## 실행 근거

- `python -X utf8 -m unittest discover -s validation -p test_product_context.py -v`: 3 tests OK. 11개 부적합 기록 변형(옵션·미검수·원본/검수 해시·근거·승인·중복 계수·경로 등), 변경/누락 파일을 차단했다.
- `python -X utf8 plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/scripts/validate_context.py output/harness-demo-20260921/product-context.json`: PASS.
- `python -X utf8 scripts/package_plugin.py`: 2개 스킬, 원본/압축 해제본 모두 번들 검증 통과. Markdown 참조·버전·ZIP CRC·23개 파일 바이트 일치 확인. 전체 명령 출력과 SHA는 [package-1.11.0.json](package-1.11.0.json).
- S1 원격 브랜치 codex/s1-intake는 `1154d259ab1fc3fb21b494090cdf42b92949b5d3`으로 원격 조회 확인했다.

## 직접 제작·열람

로컬 작업 폴더는 `output/harness-demo-20260921/`. 원본/생성물은 Git 대상에서 제외한다. `source/tray-reference.png`는 image_gen에서 생성한 가상 3칸 트레이이며, `cutout-01.png`는 그 이미지의 배경 제거 편집 결과다. 생성 결과를 직접 열람했다. 프롬프트 요약은 prompts.json, 실제 파일·원본·검수 해시는 product-context.json에 기록했다.

누끼는 RGBA 1254×1254, 알파 범위 0~255이며 완전 투명 픽셀 972,707개다. 내부의 주요 알파는 253~254로 거의 불투명하며 실제 검정/체커보드 배경을 그린 이미지가 아니다. 원본의 긴 뒤 칸 하나·앞 칸 둘·라운드 외곽·색상이 유지됐다. 소재·치수·방수·내구성은 주장하지 않았다. 독립 크리틱은 별도 원문으로 기록한다.

기록 검사 통과는 시각 품질이나 실물 동일성을 자동 보증하지 않는다. 다른 제품·가는 섬유·투명 재질은 각 실제 입력에서 별도 검수한다.

## 최종 S2 판정

구현·형식·인계·배포 검사는 통과했으나 **실제 누끼의 색상 보존은 FAIL**이다. 초기 독립 크리틱 후 두 번 수정했다. 첫 수정은 바깥쪽 번짐으로 제외했고, 두 번째는 실제 알파·형상을 유지했지만 앞면 대표 RGB 중앙값이 원본 (111,125,143) 대비 (115,133,157)로 밝고 푸른 변화가 남았다. cutout-final을 failed로 기록하고 후속 참조에서 제외했다. 원본을 기준으로 독립 S3 이후를 계속한다. 누끼에 한해 원본 픽셀 마스킹을 허용할지 사용자에게 확인 중이며 전체 완료 게이트는 열려 있다.
