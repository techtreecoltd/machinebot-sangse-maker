---
name: machinebot-product-cutout
description: 제품 원본 사진에서 흰색 스튜디오 제품 마스터컷을 여러 각도로 독립 제작·검수한다. Use for ecommerce product cutouts, 제품 기준컷, white-background studio product shots. 원본에 보이는 형상과 인쇄를 보존하고 요청한 자산만 전달한다.
---

# 제품 사진·누끼

시작할 때 [공통 제작 계약](../machinebot-ecommerce-studio/references/production-contract.md), [제품 기록](../machinebot-ecommerce-studio/references/product-context.md), [제품 스튜디오 마스터컷](../machinebot-ecommerce-studio/references/studio-product-shots.md)을 읽는다. 진입 스킬의 질문·추천 메뉴를 다시 실행하지 않는다.

1. 첨부된 제품 원본을 직접 연다. 제품 옵션, 보존할 형상·색·로고·라벨, 가려진 면을 구분한다. 제품을 확인할 수 없으면 필요한 사진만 요청한다. 단순 누끼에 고객 분석·상세 카피·전체 스펙을 요구하지 않는다.
2. 기본은 사용 가능한 원본 각도에서 흰색 스튜디오 제품컷 1~4장이다. “한 장” 등 명시 수량이 우선한다. 자료 없는 뒷면이나 새 부품을 상상하지 않는다. 정면·3/4·측면·상부 등 확인 가능한 각도를 서로 다른 제품 정보로 배정한다.
3. 호스트 이미지 편집으로 원본 제품을 기준 삼아 흰색 스튜디오로 재촬영한다. 제품 형상·표면·인쇄·색상은 유지하고 배경·카메라·조명·접지 그림자만 바꾼다. 프롬프트에는 중성 화이트밸런스, 큰 확산광, 깨끗한 흰 배경, 자연스러운 접지 그림자, 충분한 바깥 여백, 각도와 금지 요소를 명시한다. 투명 PNG 추출은 기본 결과가 아니며 사용자가 별도로 요청한 경우에만 추가 편집으로 기록한다.
4. [제품 스튜디오 마스터컷](../machinebot-ecommerce-studio/references/studio-product-shots.md), [이미지 제작](../machinebot-ecommerce-studio/references/image-production.md), [품질 게이트](../machinebot-ecommerce-studio/references/quality-gates.md)에 따라 원본과 결과를 직접 대조한다. 외곽 전체·가는 부품·로고·라벨·구멍·안쪽 면·색 번짐·흰 배경·조명·접지 그림자·세트 일관성을 확인한다. 파일 검사 기능이 있으면 배경 모서리가 불투명한 흰색 계열인지 확인하되, 기술 검사는 직접 시각 검수를 대체하지 않는다.
5. 실패 자산은 failed로 기록하고 원본 참조로 수정한다. 같은 오류 두 번이면 원인과 대안을 알린다. 통과한 파일만 제품 기록에 pass로 넣는다. 생성 컷은 파생 자산이며 원본을 대체하는 실물 증거가 아니다.
6. 파일·규격·원본 연결·검수 결과를 전달한다. 단독 요청이면 종료한다. 승인한 전체 패키지 또는 사용자의 후속 요청이 있으면 동일 product-context.json 경로와 통과 자산 ID를 인계한다.

예: “이 사진 누끼 한 장만” → 원본 열기 → 흰색 스튜디오 제품컷 한 장 생성 → 제품·조명·그림자·배경 확인 → 기록과 파일 전달. 이후 연출·상세페이지는 자동 시작하지 않는다.
