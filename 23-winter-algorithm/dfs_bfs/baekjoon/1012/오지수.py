from collections import deque


# dfs로 구현한 결과는 RecursionError가 떴음.
# bfs로 구현할 수 있다면 bfs를 먼저 사용하는게 좋을 듯.
def bfs(graph, i, j, visited):
    visited[i][j] = True
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque([[i, j]])
    while queue:
        i, j = queue.popleft()
        for di, dj in direction:
            if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1 and \
                    graph[i + di][j + dj] and not visited[i + di][j + dj]:
                queue.append([i + di, j + dj])
                visited[i + di][j + dj] = True


test = int(input())

for _ in range(test):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0
    for __ in range(k):
        j, i = map(int, input().split())
        graph[i][j] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                result += 1
                bfs(graph, i, j, visited)
    print(result)
