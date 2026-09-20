# S6 / 1.15.0 검증

효용·기능 시각화 독립 스킬을 추가했다. 기능 효과를 예쁘게 우회하지 않고 근거·소구·장면을 연결한다.

`scripts/package_plugin.py`: 원본/압축 해제본 6개 스킬·플러그인, 링크·버전·CRC·31개 파일 일치 통과. [실행 결과](package-1.15.0.json).

`validate_context.py output/harness-demo-20260921/product-context.json`: PASS. S1~S4 appeal record와 각 자산의 fact/source 연결을 확인했다.

호스트 image_gen으로 benefit-01~03.png를 각각 한 번씩 생성했다. 모두 RGB 1254×1254, src-tray만 제품 참조로 사용했고 실패한 누끼는 제외했다. 직접 열람한 역할은 다음과 같다.

| 파일 | 근거와 시각화 |
|---|---|
| benefit-01 | 세 칸 구조·각 칸의 물건 배치. 얇은 외곽선은 확인된 경계를 강조할 뿐 수치나 성능이 아니다. |
| benefit-02 | 열린 상부에서 클립을 집는 동작. 보이는 곳에 두고 꺼내는 구조만 설명한다. |
| benefit-03 | 이어진 칸막이의 T접점 확대. 단면·강도·소재·내구성 주장은 없다. |

실제 호출 인자·경로는 prompts.json 및 benefit-generation-calls.json, 최종 파일·해시는 product-context.json에 기록한다. 문구·선·효과는 각 이미지 호출에서 함께 렌더링했다. 이미지 파일·코드 합성은 없다. 실물 제품 성능·판매 전환·실험 증거로 사용할 수 없다.
