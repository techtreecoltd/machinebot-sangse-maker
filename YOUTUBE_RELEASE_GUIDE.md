# YouTube 공유 가이드

## 공유할 파일

최종 배포 파일은 `dist/machinebot-ecommerce-studio-1.6.1.zip`이다. 압축을 풀면 독립 사용 안내 `README.md`, `.codex-plugin/plugin.json`, `assets/`, `skills/machinebot-ecommerce-studio/`가 들어 있는 스킬 전용 플러그인 폴더가 나온다.

프로젝트의 가치, 지원 범위, 작동 흐름을 먼저 소개하려면 루트 `README.md`를 사용한다. 영상 설명란에는 저장소 링크와 함께 현재 버전 ZIP이 로컬 검수·공유용이라는 점을 적는다.

## 타이틀 이미지

- GitHub·플러그인 소개 대표 이미지: `plugins/machinebot-ecommerce-studio/assets/machinebot-title-imagegen.png`
- YouTube 영상 커버: `plugins/machinebot-ecommerce-studio/assets/machinebot-youtube-imagegen.png`
- 이미지 생성기가 만든 재사용 가능한 투명 타이포그래피 레이어: `plugins/machinebot-ecommerce-studio/assets/machinebot-service-lockup-imagegen.png`
- 김머신 GPT에서 추출한 정체성 기준 원본: `plugins/machinebot-ecommerce-studio/assets/machinebot-avatar-original.png`

타이틀 문구는 `MACHINEBOT`과 `ECOMMERCE VISUAL STUDIO` 두 줄만 사용한다. 호스트 이미지 생성기가 만든 투명 픽셀 워드마크에서 작은 노이즈 픽셀만 정리한 뒤 김머신 이미지 생성 베이스와 합성했다. YouTube 커버는 이 첫 번째 README 시안을 그대로 유지해 1280 × 720px로 맞췄다. HTML·SVG·시스템 폰트로 새 글자를 얹지 않았다.

## ChatGPT Work에서 보여줄 흐름

1. 플러그인을 설치한다.
2. 새 대화에서 `@machinebot-ecommerce-studio`를 선택한다.
3. 제품 사진과 기본 정보를 올린다.
4. 스킬이 추천하는 커머스 제작 분기 중 하나를 선택한다.
5. 상세페이지나 전체 패키지는 패널 구성안을 승인한다.
6. 이미지 생성과 한국어 카피 합성 결과를 확인한다.

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
