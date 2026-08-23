# AGENTS.md

## Mission

이 저장소는 제품 자료를 분석해 적합한 제작 분기를 추천하고, 사용자가 선택한 이커머스 판매 이미지를 생성·검수하는 ChatGPT Work · Codex 플러그인을 관리한다.

범위는 다음 여섯 분기로 고정한다.

1. 메인·서브 썸네일
2. 누끼컷
3. 연출·실사용컷
4. 효용·기능 시각화컷
5. 6~10장 상세페이지 이미지
6. 전체 이미지 패키지

포스터, 캐릭터, 게임, UI, 순수 일러스트 등 범용 이미지 작업을 새 분기로 추가하지 않는다.

## Source of truth

- 플러그인 소스: `plugins/machinebot-ecommerce-studio/`
- 실행 오케스트레이션: `plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/SKILL.md`
- 플러그인 메타데이터와 버전: `plugins/machinebot-ecommerce-studio/.codex-plugin/plugin.json`
- 분기별 산출물: `plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/references/branches.md`
- 상세페이지 패널 구조: `plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/references/detail-page-blueprint.md`
- 이미지 제작 절차: `plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/references/image-production.md`
- 검수 기준: `plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio/references/quality-gates.md`
- 행동 검증: `validation/behavior-evaluation.md`

`validation/package-check*/`는 배포 ZIP을 풀어 검증한 스냅샷이다. 이 경로의 파일을 원본처럼 직접 수정하지 않는다.

## Before changing anything

1. `README.md`와 이 파일을 읽어 제품의 가치와 범위를 확인한다.
2. `plugin.json`과 `SKILL.md`를 끝까지 읽는다.
3. 변경 대상에 직접 관련된 `references/` 문서만 추가로 읽는다.
4. 기존 `validation/` 시나리오가 보장하는 동작을 확인한다.
5. 사용자가 제공한 변경과 무관한 파일은 건드리지 않는다.

## Non-negotiable behavior

- 사용자 제품 사진, 로고, 패키지 문구와 검증된 정보를 기준 원본으로 취급한다.
- 효능, 인증, 수치, 원산지, 순위, 리뷰, 비교 우위, 의학·건강 주장을 발명하지 않는다.
- 모호한 요청에는 적합한 분기 2~3개만 이유와 함께 제안한다.
- 사용자가 분기를 지정했다면 전체 메뉴 선택을 다시 강요하지 않는다.
- 상세페이지와 전체 패키지는 구성안을 한 번 승인받고 생성한다.
- 상세페이지는 6·8·10장 중 하나이며, 패널당 기본 1080 × 2160px, 최소 세로 2000px, 마지막 패널 FAQ를 유지한다.
- 제품 정체성이 중요하면 신규 생성보다 사용자 제품 사진 기반 편집을 우선한다.
- 긴 한국어 카피는 텍스트 없는 이미지 베이스와 결정적 합성을 분리한다.
- 결과 이미지를 직접 확인하지 못했다면 완성 또는 검수 완료라고 말하지 않는다.
- 호스트 이미지 생성 기능이 없으면 실제 생성 사실을 주장하지 않는다.

## Change map

| 변경 의도 | 함께 확인할 파일 |
| --- | --- |
| 트리거·대화 흐름 | `SKILL.md`, `agents/openai.yaml`, `validation/behavior-evaluation.md` |
| 분기·수량 | `branches.md`, `README.md`, 플러그인 `README.md` |
| 상세페이지 규격 | `detail-page-blueprint.md`, `image-production.md`, `quality-gates.md`, 행동 검증 |
| 이미지 제작 방법 | `image-production.md`, `quality-gates.md`, `SKILL.md` |
| 브랜드·타이틀 이미지 | 플러그인 `assets/`, 두 README, `YOUTUBE_RELEASE_GUIDE.md`, `plugin.json`, `agents/openai.yaml` |
| 표시 이름·설명·버전 | `.codex-plugin/plugin.json`, 두 README, `CHANGELOG.md`, 배포 ZIP |
| 공개 데모·영상 | `YOUTUBE_RELEASE_GUIDE.md`, 배포 ZIP |

핵심 동작을 바꿀 때는 관련 문서와 검증을 같은 변경에서 맞춘다. 문서에만 존재하고 스킬이 수행하지 못하는 기능을 약속하지 않는다.

## Editing and packaging rules

- 플러그인 실행 원본은 `plugins/machinebot-ecommerce-studio/`에서만 수정한다. 루트 README와 배포 문서는 이 원본의 현재 동작을 설명하도록 함께 맞춘다.
- 플러그인 내부 구조는 `.codex-plugin/`, `skills/`, 선택적 `assets/`를 유지한다.
- 새 참고 문서는 `references/`에 두고 `SKILL.md`에서 언제 읽는지 명시한다.
- 배포 콘텐츠가 바뀌면 `plugin.json`의 semver를 올리고 README, 변경 기록, ZIP 이름을 함께 맞춘다.
- 기존 배포 ZIP을 덮어쓰기보다 새 버전 파일을 `dist/`에 만든다.
- ZIP은 `machinebot-ecommerce-studio/` 폴더를 최상위에 포함해야 한다.
- API 키, 로컬 이미지 모델, 외부 생성 스크립트를 필수 의존성으로 추가하지 않는다. 이미지 실행은 호스트 기능을 사용한다.
- `assets/machinebot-avatar-original.png`를 김머신 봇 정체성 기준 원본으로 취급한다. 새 타이틀 이미지를 만들 때 얼굴, 머리, 안경, 은색 안드로이드 구조, 청색 눈과 회로를 임의로 재설계하지 않는다.
- 브랜드 타이틀은 `MACHINEBOT`과 `ECOMMERCE VISUAL STUDIO` 두 줄의 평면 픽셀 워드마크를 사용한다. 호스트 이미지 생성기로 투명 PNG 글자를 직접 만들며, HTML·SVG·캔버스·시스템 폰트 API로 새 글자를 렌더링하지 않는다.
- 생성된 투명 타이포그래피 PNG는 생성 배경과 이미지 대 이미지로 합성하고, 최종 단일 PNG를 직접 열어 철자·투명도·가독성을 확인한다.
- README 상단에는 HTML 레이어, HTML 정렬 래퍼, 별도 HTML 제목을 사용하지 않는다. 모든 타이포그래피를 최종 PNG 안에 평탄화하고 순수 Markdown 이미지 문법으로 한 장만 참조한다.

## Validation

Windows PowerShell에서 최소 다음 검증을 실행한다.

```powershell
$env:PYTHONUTF8 = "1"
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "plugins\machinebot-ecommerce-studio\skills\machinebot-ecommerce-studio"
python "$env:USERPROFILE\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" "plugins\machinebot-ecommerce-studio"
```

그다음 새 ZIP을 별도의 `validation/package-check-<version>/` 경로에 풀고, 압축 해제본에도 같은 두 검증을 반복한다. README 링크, manifest 버전, ZIP 파일명도 확인한다.

행동 변경이 있다면 `validation/behavior-evaluation.md`의 대표 시나리오를 갱신하거나 새 시나리오를 추가한다. 최소한 다음을 계속 보장해야 한다.

- 탐색 요청의 추천 흐름
- 명시적 분기의 직행 흐름
- 전체 패키지의 라이트·풀 선택
- 근거 없는 주장 차단
- 제품 정체성 보존
- 상세페이지 규격과 마지막 FAQ
- 범용 이미지 요청의 범위 거절

## Completion checklist

- 요청된 파일과 동작이 모두 존재한다.
- 핵심 문서 사이에 범위·수량·버전 충돌이 없다.
- 원본 플러그인과 압축 해제본 검증이 모두 통과한다.
- 새 배포 ZIP과 체크섬이 준비되어 있다.
- 공개 디렉토리 등록을 실제로 하지 않았다면 등록 완료라고 표현하지 않는다.
