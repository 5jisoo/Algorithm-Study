from collections import deque

def bfs(area, i, j, visited):
    global direction
    queue = deque([[i, j]])
    visited[i][j] = True
    count = 1
    while queue:
        start_row, start_col = queue.popleft()
        for d_row, d_col in direction:
            next_row, next_col = start_row + d_row, start_col + d_col
            if 0 <= next_row < n and 0 <= next_col < n and area[next_row][next_col] \
                and not visited[next_row][next_col]:
                count += 1
                queue.append([next_row, next_col])
                visited[next_row][next_col] = True
    return count


n = int(input())
area = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

result = 0
result_list = []
for i in range(n):
    for j in range(n):
        if area[i][j] and not visited[i][j]:
            result += 1
            result_list.append(bfs(area, i, j, visited))

result_list.sort()
print(result)
for r in result_list:
    print(r)