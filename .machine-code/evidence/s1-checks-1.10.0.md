# S1 실제 검사 출력 요약

2026-09-21. 단계 범위는 최소 질문·타입 추천·기존 분기 연결과 공수 산정이다. 새로운 이미지 생성은 실행하지 않았다.

## 원본

```text
python .../skill-creator/scripts/quick_validate.py plugins/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio
Skill is valid!
exit: 0

python .../plugin-creator/scripts/validate_plugin.py plugins/machinebot-ecommerce-studio
Plugin validation passed: C:\Users\gimma\Documents\dev\machienbot-sangse-maker\plugins\machinebot-ecommerce-studio
exit: 0
```

`...`는 설치된 `C:/Users/gimma/.codex/skills/.system` 경로다. Python UTF-8 모드로 실행했다.

## 압축 해제본

```text
python .../skill-creator/scripts/quick_validate.py validation/package-check-1.10.0/machinebot-ecommerce-studio/skills/machinebot-ecommerce-studio
Skill is valid!
exit: 0

python .../plugin-creator/scripts/validate_plugin.py validation/package-check-1.10.0/machinebot-ecommerce-studio
Plugin validation passed: C:\Users\gimma\Documents\dev\machienbot-sangse-maker\validation\package-check-1.10.0\machinebot-ecommerce-studio
exit: 0
```

## 파일·문서·산술

- ZIP 실제 검사 값: [package-1.10.0.json](package-1.10.0.json).
- 원본과 압축 해제본 18개 파일의 바이트 일치, ZIP CRC·최상위 폴더·SHA-256·manifest 아이콘·버전 검사 통과.
- 패키지 양쪽의 Markdown 링크 38개 검사 통과.
- 목표·PRD·공수·README·AGENTS·계획·대화 원문 문서의 링크 40개 검사 통과.
- 공수 합계 39~64h, 예비 포함 47~84h, S4까지 26~42h·예비 포함 32~55h, 패널 재시도 예시 산술 검사 통과.
- 가상 사례 ID 15개와 독립 응답 원문 15개 대응 확인. 내용 판정은 검사 코드의 ID 대응만으로 대신하지 않는다.
- `git diff --check` 종료 코드 0. Windows 줄바꿈 안내는 있었으나 공백 오류는 없었다.
- S0 종료 시점 원본 17개 파일의 해시와 비교해 manifest·플러그인 README·SKILL·openai.yaml·branches의 5개 변경과 intake-routing 신규 1개를 확인했다. 그 밖의 제작 참조와 브랜드 이미지 바이트는 유지됐다.

## 행동 실행 원문

[15개 사례 입력](../../validation/intake-cases-1.10.0.json), [반환 문안](../../validation/intake-forward-test-1.10.0.md). 새 맥락의 에이전트에 실행 스킬·참조·가상 입력만 제공했다. 실제 호스트 UI 조작·이미지 생성·정체성 보존·텍스트 정확성의 실측은 포함하지 않는다.
