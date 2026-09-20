# Machine Code 설치 기록

확인일: 2026-09-21. 범위: 개발 스킬 설치·프로젝트 운영 준비. 이 기록은 제품 하네스 구현이나 이미지 품질 완료 증거가 아니다.

## 출처와 설치

- 사용자 지정 저장소: `techtreecoltd/machine-code` (GitHub 인증으로 접근한 비공개 저장소).
- 패키지 버전: 0.3.0.
- 설치 리비전: `a58586aab95615df28a8943b05b8b9dc9fc7e31c`.
- 설치 위치: 사용자 Codex 홈의 `skills/machine-code`, `skills/skill-creator2`, `skills/harness-creator`.
- 설치 방법: 번들 `skill-installer/scripts/install-skill-from-github.py`에 위 세 경로, 지정 리비전, `--method git` 전달.
- 런타임: Node v24.13.1. 원본 요구사항은 Node 20 이상이며 별도 npm 런타임 의존성은 없다.

## 기존 설정 보존

기존 `harness-creator`는 `detail-factory/skills/harness-creator`를 가리키는 깨진 Windows junction이었다. `SKILL.md`를 읽을 수 없는 상태를 확인하고 해당 연결을 사용자 Codex 홈의 `skill-backups/harness-creator-broken-20260921`로 이동했다. 같은 위치의 `.json`에 기존 대상 정보를 보관했다. 대상 프로젝트 파일은 삭제·수정하지 않았다.

저장소의 `global/AGENTS.machine-code.md` 관리 블록을 사용자 전역 `AGENTS.md`에 추가했다. 기존 본문을 보존하고 `skill-backups/AGENTS.before-machine-code-20260921.md`에 원본을 백업했다. 번들 시스템 스킬은 수정하지 않았다.

## 실행한 설치 검증

| 검사 | 실제 결과 |
|---|---|
| 세 스킬의 번들 `quick_validate.py` | 각각 `Skill is valid!`, 종료 코드 0 |
| 세 스킬 CLI의 `help` | 각각 도움말 출력, 종료 코드 0; 형제 스킬 import 성공 |
| Git 트리와 설치 파일 대조 | machine-code 12개, skill-creator2 5개, harness-creator 5개 일치 |
| 대조 방법 | 지정 리비전의 blob SHA와 로컬 파일 대조. Windows CRLF/LF 변환만 정규화 허용 |
| 프로젝트 작업 공간 초기화 | `init --profile project` 종료 코드 0 |

## 프로젝트 적용 범위

- 작업 기준은 `docs/harness-goals.md`와 `docs/harness-prd.md`다.
- `.machine-code/plan.md`에 직렬 순서·설계 컨펌·검증·최종 독립 감사 조건을 연결한다.
- 현재 목표는 하네스 보강 전체다. 설치 완료와 S0 문서 작업을 전체 목표 완료로 표시하지 않는다.
- 목표 도구 기록은 생성하지 않았다. helper의 초기 `codex-define-goal` 값은 목표 문서 작성 흐름에 대응하는 자동 메타데이터이며 목표 도구 호출의 증거가 아니다.
- 새 스킬은 다음 사용자 턴부터 자동 발견 대상이다. 이번 턴에는 설치된 스킬 파일을 직접 읽고 적용했다.
- CLI는 설치된 스킬의 `.mjs`를 Node로 실행한다. 전역 npm 명령 등록은 별도로 하지 않았다.

S1 설계 승인이 다음 사용자 결정이다. 원본 제품 플러그인의 실행 내용·manifest 버전·배포 ZIP은 이번 설치에서 변경하지 않는다.
