# 단계별 Git 푸시

사용자 승인: “작업 분기마다 깃에 푸시하고, 품질체크하고 크리틱하고 직접 결과물도 만드는 방식으로 끝까지”. 같은 작업 트리에서 직렬로 구현하며 각 브랜치는 직전 단계 커밋을 포함한다. main 자동 병합·강제 푸시·공개 플러그인 등록은 범위가 아니다.

| 단계 | 원격 브랜치 | 확인한 커밋 | 검증 |
|---|---|---|---|
| S1 | codex/s1-intake | 1154d259ab1fc3fb21b494090cdf42b92949b5d3 | push 성공 후 ls-remote 일치 |
| S2 | codex/s2-cutout | b5c025bb6a84569e03c7028fd638ea100d708481 | push 성공 후 ls-remote 일치; 실제 색상 보존 FAIL 공개 기록 |
| S3 | codex/s3-lifestyle | 676648e1330e26d64ce60d6681e9150153ffb327 | push 성공 후 ls-remote 일치 |
| S4 | codex/s4-detail | 746a2b831d1e5853c182dd7b6a2bfa9c4a9168bd | push 성공 후 ls-remote 일치; 6장 상세페이지 직접 검수 |
| S5 | codex/s5-thumbnail | 0cbc199803685121ea573f0d3c73f236f90bc801 | push 성공 후 ls-remote 일치; appeal 매핑 수정 후 독립 크리틱 통과 |
| S6 | codex/s6-benefit | b9b8ce081a2b012a0052bfe92c33e8b766eb7144 | push 성공 후 ls-remote 일치; 효용 3장 직접 검수 |
| S7 | codex/s7-package | d1dee3324d622bcbb46ff2b86ee56658d2848caa | push 성공 후 ls-remote 일치; 1.16.3 패키지 게이트·부분 manifest·독립 크리틱 진행 |
| S8 | codex/s8-cg-visualization | pending | CG 판단 카탈로그·실제 합성 fixture·독립 크리틱 후 푸시 예정 |

생성 결과·고객 자료는 로컬 output/에 보관한다. Git에는 플러그인 소스·배포 ZIP·검증 기록을 올린다.
