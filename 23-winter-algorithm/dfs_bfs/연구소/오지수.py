'''
조합을 사용해야 된다는 점까지는 접근함.
조합 전에 추가적인 알고리즘을 사용해 전처리를 해주어야 된다고 생각 했으나, 
모든 경우의 수를 확인해도 시간 내에 가능하다는 점을 확인한 뒤 문제를 다시 풀었음.
(이 과정을 거치느라 문제 자체는 오랫동안 풀었음.)
'''
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = []
virus = []
none = []  # 빈 공간 좌표 저장
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            none.append([i, j])


def check(virus, visited):
    queue = deque(virus)
    cnt = 0
    while queue:
        start_row, start_col = queue.popleft()
        visited[start_row][start_col] = True
        for d_row, d_col in direction:
            next_row, next_col = start_row + d_row, start_col + d_col
            if 0 <= next_row < n and 0 <= next_col < m and not graph[next_row][next_col] \
                    and not visited[next_row][next_col]:
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and not graph[i][j]:
                cnt += 1
    return cnt


result = 0
data = list(combinations(none, 3))
for d in data:
    for i, j in d:  # 벽 설정
        graph[i][j] = 1
    visited = [[False] * m for _ in range(n)]
    result = max(check(virus, visited), result)
    for i, j in d:  # 벽 설정 제거
        graph[i][j] = 0

print(result)
