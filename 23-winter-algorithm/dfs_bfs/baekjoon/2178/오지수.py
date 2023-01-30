from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
queue = deque([[0, 0]])

while queue:
    start_row, start_col = queue.popleft()
    for d_row, d_col in directions:
        next_row, next_col = start_row + d_row, start_col + d_col
        if 0 <= next_row < n and 0 <= next_col < m and maze[next_row][next_col] == 1:   # 이동 가능한 범위 내에 있음.
            if next_row == 0 and next_col == 0:
                continue
            maze[next_row][next_col] = maze[start_row][start_col] + 1   # 방문 처리
            queue.append([next_row, next_col])

print(maze[n-1][m-1])


