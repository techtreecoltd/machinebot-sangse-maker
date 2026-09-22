# 단계별 Git 푸시

사용자 승인: “작업 분기마다 깃에 푸시하고, 품질체크하고 크리틱하고 직접 결과물도 만드는 방식으로 끝까지”. 각 브랜치는 직전 단계 커밋을 포함한다. 이후 “아니 메인에 푸시를 해 이제”로 main 반영도 승인됐다. 강제 푸시·공개 플러그인 등록은 수행하지 않는다. S9는 기존 작업 폴더의 미추적 산출물을 보존하고 origin/main 기반의 별도 작업 트리에서 직렬로 수정한다.

| 단계 | 원격 브랜치 | 확인한 커밋 | 검증 |
|---|---|---|---|
| S1 | codex/s1-intake | 1154d259ab1fc3fb21b494090cdf42b92949b5d3 | push 성공 후 ls-remote 일치 |
| S2 | codex/s2-cutout | b5c025bb6a84569e03c7028fd638ea100d708481 | push 성공 후 ls-remote 일치; 실제 색상 보존 FAIL 공개 기록 |
| S3 | codex/s3-lifestyle | 676648e1330e26d64ce60d6681e9150153ffb327 | push 성공 후 ls-remote 일치 |
| S4 | codex/s4-detail | 746a2b831d1e5853c182dd7b6a2bfa9c4a9168bd | push 성공 후 ls-remote 일치; 6장 상세페이지 직접 검수 |
| S5 | codex/s5-thumbnail | 0cbc199803685121ea573f0d3c73f236f90bc801 | push 성공 후 ls-remote 일치; appeal 매핑 수정 후 독립 크리틱 통과 |
| S6 | codex/s6-benefit | b9b8ce081a2b012a0052bfe92c33e8b766eb7144 | push 성공 후 ls-remote 일치; 효용 3장 직접 검수 |
| S7 | codex/s7-package | d1dee3324d622bcbb46ff2b86ee56658d2848caa | push 성공 후 ls-remote 일치; 1.16.3 패키지 게이트·부분 manifest·독립 크리틱 진행 |
| S8 | codex/s8-cg-visualization | 9cc15f9cd0a52f9fc3a6f6cd36675128f60e1d66 | CG 판단 카탈로그·실제 합성 fixture·독립 크리틱 완료 후 원격 브랜치 확인 |
| S9 | codex/s9-studio-cutout 및 main | feddd5e89c2e2bdad48de797278aa7e1228f4e29 | 1.17.1 원본·배포본·13개 테스트·합성 3각도 독립 검토 후 atomic fast-forward push 성공, 두 원격 ref의 ls-remote 일치 |

S9 구현 커밋의 main 반영은 2026-09-22 확인했다. critic-s9-final.md의 `main push pending`은 감사 시점의 상태이며 위 실제 푸시로 해소했다. 이 기록을 추가한 후속 커밋은 제품 코드를 바꾸지 않는다. 과거 전체 프로젝트 미완료 판정과 구분한다.

생성 결과·고객 자료는 로컬 output/에 보관한다. Git에는 플러그인 소스·배포 ZIP·검증 기록을 올린다.
