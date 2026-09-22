# YouTube 공유 가이드

## 공유할 파일

최종 배포 파일은 `dist/machinebot-ecommerce-studio-1.18.0.zip`이다. 압축을 풀면 독립 사용 안내 `README.md`, `.codex-plugin/plugin.json`, `assets/`, `skills/machinebot-ecommerce-studio/`가 들어 있는 스킬 전용 플러그인 폴더가 나온다.

프로젝트의 가치, 지원 범위, 작동 흐름을 먼저 소개하려면 루트 `README.md`를 사용한다. 영상 설명란에는 저장소 링크와 함께 현재 버전 ZIP이 로컬 검수·공유용이라는 점을 적는다.

## 타이틀 이미지

- GitHub·플러그인 소개 대표 이미지: `plugins/machinebot-ecommerce-studio/assets/machinebot-title-imagegen.png`
- YouTube 영상 커버: `plugins/machinebot-ecommerce-studio/assets/machinebot-youtube-imagegen.png`
- 김머신 GPT에서 추출한 정체성 기준 원본: `plugins/machinebot-ecommerce-studio/assets/machinebot-avatar-original.png`

타이틀 문구는 `MACHINEBOT`과 `ECOMMERCE VISUAL STUDIO` 두 줄만 사용한다. 새 타이틀이나 커버는 캐릭터·배경·픽셀 워드마크 전체를 호스트 이미지 생성기의 한 번의 호출로 만들며, 투명 타이포그래피 PNG나 HTML·CSS·SVG·캔버스·시스템 폰트 합성을 사용하지 않는다. 기존 파일은 과거 공개 시안의 최종 평탄화 자산으로만 보존하고 분리된 글자 자산을 새 제작에 재사용하지 않는다.

## ChatGPT Work에서 보여줄 흐름

1. 플러그인을 설치한다.
2. 새 대화에서 `@machinebot-ecommerce-studio`를 선택한다.
3. 제품 사진과 기본 정보를 올린다.
4. 부족한 정보만 답하고 총 2~3개 추천 중 하나를 선택한다. 이미 타입을 지정했다면 추천 메뉴 없이 직행한다.
5. 고객 가치·근거·핵심 소구와 이를 보여줄 장면을 확인하고, 상세페이지나 전체 패키지는 구성안을 한 번 승인한다.
6. 패널별 한 번의 이미지 생성 호출로 완성된 한국어 카피·제품 정체성·장점 시각화를 확인한다.
7. 전체 결과를 나란히 보며 같은 장면 반복 없이 각 장이 새로운 구매 정보를 전달하는지 확인한다.

중국어·일본어 등 외국어 상세페이지 ZIP을 데모할 때는 원본 이미지를 최종 배경으로 재사용하지 않는다. 제품과 기능 구조를 추출한 뒤, 호스트 이미지 생성 기능으로 원문을 제거하고 한국어 카피까지 직접 렌더링하는 흐름을 보여준다.

## 영상 데모 프롬프트

탐색형:

> @machinebot-ecommerce-studio 신제품 텀블러를 판매하려고 해. 어떤 커머스 이미지를 만드는 게 좋은지 추천해 줘.

상세페이지 직행형:

> @machinebot-ecommerce-studio 이 제품 사진과 스펙으로 8장짜리 한국형 상세페이지를 만들어 줘. 각 장은 세로 2000px 이상이어야 해.

전체 패키지형:

> @machinebot-ecommerce-studio 이 제품의 누끼, 메인·서브 썸네일, 연출컷, 효용 시각화컷, 상세페이지까지 전체 패키지로 진행해 줘.

## 배포 경로 주의

압축 파일은 소스·검수·로컬 테스트용 배포본이다. ChatGPT Work 웹·모바일 사용자가 플러그인 목록에서 바로 설치하게 하려면 OpenAI의 universal plugin directory 제출·승인 절차가 별도로 필요하다. 공개 전에 로컬 marketplace에서 설치하고 새 대화로 대표 요청을 테스트한다.

공식 문서:

- Skills: https://learn.chatgpt.com/docs/build-skills
- Plugins: https://learn.chatgpt.com/docs/build-plugins

독립 누끼: `$machinebot-product-cutout 이 제품 사진으로 흰색 스튜디오 제품컷 한 장을 만들어 줘.` 다른 제작도 원본과 검수 자산을 product-context.json으로 이어 받을 수 있습니다. 투명 PNG가 필요하면 별도 추가 요청으로 기록합니다.

연출·실사용컷을 machinebot-lifestyle로 분리하고 원본·검수 자산을 재사용한다. 단독 연출은 상세페이지로 자동 확장하지 않는다.

상세페이지와 외국어 현지화를 machinebot-detail-page로 분리했다. 독립 자산 세트의 의무 생성 없이 구성 승인·6/8/10장·마지막 FAQ·패널 동시 렌더링을 유지한다.

메인·서브 썸네일을 machinebot-thumbnail로 분리했다. 기본 6~8장과 명시 수량·규격, 채널 규정 확인 범위, 독립 납품을 유지한다.

효용·기능 시각화를 machinebot-benefit-visual로 분리했다. 근거 있는 구조·사용 장면만 허용하고 미검증 성능 효과·숫자·비교를 차단한다.

전체 이미지 패키지 연결 계약·부분 패키지 차단 검증·제안 계획 지원

패키지 승인 상태 게이트와 전체 슬롯 회귀 테스트 보강

패키지 슬롯 중복 파일 차단과 회귀 테스트 보강

라이트 누끼 1~2장 계약과 미지원 tier 차단

추상 가치의 CG 시각화 판단을 연출·효용·상세 공통 흐름에 반영

CG 판단 카탈로그와 README·연출·효용 연결 설명 보강

CG 시각화 판단을 상세페이지 스킬까지 직접 연결하고 실제 합성 fixture 검수 기록 추가
