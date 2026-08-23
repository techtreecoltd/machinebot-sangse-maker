![MACHINEBOT — Ecommerce Visual Studio](./assets/machinebot-title-imagegen.png)

제품 사진과 사실 정보를 분석해 무엇을 만들지 먼저 제안하고, 선택한 분기를 호스트의 이미지 생성 기능으로 제작·검수하는 ChatGPT Work · Codex 플러그인입니다.

## 할 수 있는 일

1. 메인 1장과 서브 5~7장으로 구성한 썸네일 세트
2. 합성에 사용할 투명 배경 누끼컷 1~4장
3. 제품 단독 연출과 실제 사용 상황을 포함한 연출·실사용컷 4~10장
4. 열·냉기·흡수·구조 같은 보이지 않는 장점을 설명하는 효용 시각화컷 3~6장
5. 패널당 세로 2000px 이상인 6·8·10장 한국형 상세페이지
6. 위 자산을 하나의 시각 시스템으로 묶은 라이트·풀 전체 패키지

무엇이 필요한지 아직 정하지 않았다면 제품에 적합한 분기 2~3개를 이유와 함께 제안합니다. 이미 결과물을 지정했다면 불필요한 메뉴 선택 없이 해당 분기로 바로 진행합니다.

## 사용 예시

ChatGPT Work:

```text
@machinebot-ecommerce-studio 이 제품 사진을 보고
판매에 필요한 커머스 이미지 분기를 추천해 줘.
```

Codex:

```text
$machinebot-ecommerce-studio 이 제품의 8장 상세페이지를 만들어 줘.
제품 모양과 패키지 문구는 참조 사진 그대로 유지해 줘.
```

상세페이지와 전체 패키지는 패널 또는 자산 구성안을 먼저 보여주고 한 번 승인받은 뒤 이미지 생성에 들어갑니다.

## 준비하면 좋은 자료

- 제품명, 카테고리, 핵심 고객과 판매 채널
- 정면·측면·패키지 사진과 로고·브랜드 자료
- 검증된 특징, 스펙, 사용법, 주의사항과 인증 근거
- 선호·금지 색감, 참고 이미지, 반드시 넣을 정확한 문구
- 필요한 비율, 픽셀 크기와 파일 형식

모든 자료가 없어도 시작할 수 있습니다. 이미 제공된 내용은 다시 묻지 않고, 선택한 분기를 만드는 데 실제로 부족한 항목만 요청합니다.

## 제작 원칙

- 제품 사진과 검증된 사실을 기준 원본으로 사용합니다.
- 효능, 인증, 수치, 리뷰, 순위, 비교 우위를 임의로 만들지 않습니다.
- 제품 정체성이 중요한 경우 신규 생성보다 참조 이미지 편집을 우선합니다.
- 기본 상품컷은 중성 흰색 스튜디오, 정확한 화이트 밸런스와 깨끗한 그림자를 사용합니다.
- 중국어·일본어 등 외국어 상세페이지는 원문의 제품·기능 구조만 추출하고, 이미지 생성 단계에서 원문 제거와 한국어 카피 렌더링을 함께 처리합니다.
- 외국어 현지화 분기에서는 HTML·SVG·캔버스·코드 폰트로 한국어를 덮어쓰지 않습니다.
- 생성한 결과를 직접 확인하지 못하면 검수 완료라고 말하지 않습니다.

## 패키지 구조

```text
machinebot-ecommerce-studio/
├─ .codex-plugin/plugin.json
├─ assets/
│  ├─ machinebot-avatar-original.png
│  ├─ machinebot-service-lockup-imagegen.png
│  ├─ machinebot-title-imagegen.png
│  └─ machinebot-youtube-imagegen.png
├─ README.md
└─ skills/machinebot-ecommerce-studio/
   ├─ SKILL.md
   ├─ agents/openai.yaml
   ├─ assets/icon.svg
   └─ references/
      ├─ branches.md
      ├─ detail-page-blueprint.md
      ├─ image-production.md
      ├─ source-detail-localization.md
      └─ quality-gates.md
```

에이전트는 `SKILL.md`를 실행 규칙의 기준으로 사용하고, 현재 분기에 필요한 `references/` 문서만 조건부로 읽습니다.

## 범위 밖

이 플러그인은 상품 판매 자산 전용입니다. 포스터, 캐릭터, 게임, UI, 순수 일러스트와 상품 판매에 무관한 범용 이미지 편집은 다루지 않습니다.

실제 이미지 생성에는 ChatGPT Work 또는 Codex 호스트의 이미지 생성·편집 기능이 필요합니다. 호스트에 해당 기능이 없으면 이미지 프롬프트와 제작 명세까지만 제공하며, 생성했다고 주장하지 않습니다.
