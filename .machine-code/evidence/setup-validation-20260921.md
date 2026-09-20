# Machine Code 적용 확인

확인일: 2026-09-21. 범위: 설치·문서·작업 공간 준비(S0). S1~S7 제품 구현과 이미지 품질은 검증하지 않았다.

## 실행 결과

- 목표·PRD·계획·인계·설치 기록·README·AGENTS의 7개 Markdown 문서를 UTF-8로 읽고 코드 블록 균형·미완성 scaffold 마커·로컬 링크를 검사했다. 33개 링크가 존재하며 A01~A17 시나리오 ID가 중복 없이 유지된다.
- `init --profile project`, `checkpoint --stage understand`, `resume --write`, `status --json`이 종료 코드 0으로 실행됐다.
- `state.json`은 `project / understand`다. `design`, `execute`, `complete` 체크포인트가 없음을 확인했다. S1 설계 승인 전 구현하지 않는 상태다.
- `verify --json`은 예상대로 종료 코드 2, `ready: false`를 반환했다. 미실행 단계와 제품 구현·감사·검증·최종 인계 증거가 부족하며 계획은 사용자 승인 대기로 `unknown`이다. 참조한 증거 파일의 누락·stale 오류는 없었다. 출력은 로컬 전용 `.machine-code/runs/verify-initialization.json`에 보관했다.
- `plugins/machinebot-ecommerce-studio/`의 기존 17개 파일을 SHA-256으로 전후 비교했다. 추가·변경·삭제가 없었다.
- `git diff --check -- AGENTS.md README.md`는 종료 코드 0이다. 첫 검사에서 `core.autocrlf=false`를 임시 지정했을 때 기존 CRLF가 공백 오류로 표시돼, 저장소의 실제 줄바꿈 설정으로 재검사했다. 파일 전체의 줄바꿈을 바꾸는 수정은 하지 않았다.
- 세 설치 스킬의 유효성, CLI import, 지정 리비전의 22개 파일 일치는 [설치 기록](installation-20260921.md)에서 확인한다.

## 판정과 다음 행동

개발 도구 설치와 프로젝트 적용 준비는 확인됐다. 전체 하네스 보강 목표는 미완료이며 설치 검증을 제품 검증으로 대체하지 않는다.

다음 사용자 결정은 PRD §4·§10의 S1 설계다. 최소 질의응답 → 총 2~3개 추천 → 선택한 기존 제작 경로 연결, 명시 요청 직행을 첫 범위로 제안한다. 승인 후 해당 범위의 구현·동작 평가·배포 검증을 수행한다.
