# Algorithm Study

> 알고리즘 스터디를 위한 저장소입니다.
> 
- 기간: 2023년 1월 2일 ~
- 정기 회의: 월요일 오후 10시
- 공부 자료: 이것이 취업을 위한 코딩 테스트다 with 파이썬
- 언어: ```python```
- 스터디원
    
    
    |  | 신진영 | 오지수 | 정지원 | 조영서 |
    | --- | --- | --- | --- | --- |
    | GitHub | [Jjinyshin](https://github.com/Jjinyshin) | [5jisoo](https://github.com/5jisoo) | [codeJiwon](https://github.com/codeJiwon) | [dudrhy12](https://github.com/dudrhy12) |

<br>

## 스터디 규칙

- **매주 일요일 오전 9시** 이전까지 각자 브랜치에서 문제를 풀고, 커밋해서 PR을 보냅니다.
- PR이 들어오면 **정기 회의 시간** 이전까지 다른 사람이 푼 문제 중 한 문제씩 선점하여 코드 리뷰를 남겨야 합니다.
    - 정기 회의 시간엔 각자 작성한 코드 리뷰를 설명해야 합니다.
- 주 9시간 이상 공부하고 교재 개념 학습 뒤 문제 풀이를 진행합니다.
    - 권장 시간: 개념학습 3h / 문제 풀이 6h

<br>

## PR(Pull Request) 규칙

- 모두에게 리뷰를 받았을 때 (총 3번) ```Merge```가 가능합니다.
- `Merge` 버튼은 모두에게 `Approve` 리뷰를 받았을 때, 마지막 리뷰어가 누르는 것으로 합니다.
- 제목 및 내용은 자유롭게 설정합니다.

<br>

## Commit 규칙

- Branch 생성: `자신의 이름(혹은 아이디)`
- Commit Message는 다음을 참고합니다.
    - ➕ [ADD] : 문제 풀이 파일이나 부수적인 코드 추가
    - ☑️ [MOD] : 코드 및 내부 파일 수정
    - ✏️ [CORRECT] : 문법 오류 해결, 타입 변경, 이름 변경 등의 작은 수정
    - 🗑️ [DEL] : 쓸모 없는 코드 혹은 파일 삭제
    - 📝 [DOCS] : README 등의 문서 개정
    - 🚚 [MOVE] : 프로젝트 파일 및 코드 이동
    - 📛 [RENAME] : 파일 이름 변경
    - 🔀 [MERGE] : 다른 브랜치와의 충돌 해결 후 Merge
    - ♻️ [REFACTOR] : 전면 수정
        - ex) [ADD] 그리디 3번 문제

<br>

## 파일 및 폴더 구조

- `폴더명`은 <a href="#curriculum">**커리큘럼 일정**</a> 참고
- 교재에 수록된 문제를 푸는 경우
    - 23-winter-algorithm/`폴더명`/문제/`이름.py`
        - ex) 23-winter-algorithm/`greedy`/모험가 길드/신진영.py
        - 23-winter-algorithm/`sort`/나이순 정렬/오지수.py
- 외부 문제를 푸는 경우
    - 23-winter-algorithm/`폴더명`/`알고리즘 사이트`/문제 번호/`이름.py`
        - ex) 23-winter-algorithm/`greedy`/`baekjoon`/10845/정지원.py
        - 23-winter-algorithm/`greedy`/`programmers`/숫자 찾기/조영서.py

<br>

<div id="curriculum"> <div>

## 커리큘럼 일정 

| 주차 | 알고리즘 | 폴더명 |
| --- | --- | --- |
| 1주차 | 스택과 큐 | stack_queue |
| 2주차 | 그리디 | greedy |
| 3주차 | 구현 | implementation |
| 4주차 | DFS/BFS | dfs_bfs |
| 5주차 | 정렬 | sort |
| 6주차 | 이진 탐색 | binary_search |
| 7주차 | 다이나믹 프로그래밍 | dynamic_programming |
| 8주차 | 최단 경로 | shortest_path |
| 9주차 | 그래프 이론 | graph |
