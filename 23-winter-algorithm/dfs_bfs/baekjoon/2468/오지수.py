from collections import deque

n = int(input())

area = []
highest_height = 0
for _ in range(n):
    data = list(map(int, input().split()))
    area.append(data)
    highest_height = max(max(data), highest_height)

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(i, j, visited, height):
    queue = deque([[i, j]])
    visited[i][j] = True
    while queue:
        start_row, start_col = queue.popleft()
        for d_row, d_col in directions:
            next_row, next_col = start_row + d_row, start_col + d_col
            if 0 <= next_row < n and 0 <= next_col < n and area[next_row][next_col] > height \
                    and not visited[next_row][next_col]:
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True

result = 0
for height in range(highest_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visited[i][j]:
                count += 1
                bfs(i, j, visited, height)
    result = max(result, count)

print(result)