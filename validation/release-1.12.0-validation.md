# S3 / 1.12.0 검증

독립 연출·실사용 스킬, 명시 요청 직행, 제품 기록 인계. 별도 누끼·상세페이지 제작을 강제하지 않는다.

`python -X utf8 scripts/package_plugin.py`: 원본/압축 해제본의 3개 스킬·플러그인 검사, 링크·버전·CRC·25개 파일 일치 통과. [명령 출력·SHA](package-1.12.0.json).

`validate_context.py output/harness-demo-20260921/product-context.json`: PASS. 실패 누끼 두 자산은 failed이며 연출은 원본 src-tray만 참조했다.

호스트 image_gen으로 lifestyle-01~04.png를 각각 한 번씩 생성하고 직접 열람했다. 모두 RGB 1254×1254. 사용자 제품의 실물 동일성 검증이 아닌 가상 트레이의 제작 실행이다.

| 파일 | 직접 확인한 역할 |
|---|---|
| lifestyle-01 | 전체 책상 배치와 세 칸의 소지품 구분 |
| lifestyle-02 | 클립을 집는 손·자연스러운 접촉 |
| lifestyle-03 | 상부 시점에서 케이블을 제자리에 놓는 동작 |
| lifestyle-04 | 칸막이 T 접점·각 칸의 바닥 디테일 |

프롬프트 전문·원본 해시·파일 해시·검수 note는 로컬 output/harness-demo-20260921/prompts.json과 product-context.json에 보관한다. 생성물은 저장소에 올리지 않는다. 전체 세트는 원본 구조를 유지하면서 장면 역할과 시점을 구분한다. 크기·소재·기능 수치를 주장하지 않는다.
