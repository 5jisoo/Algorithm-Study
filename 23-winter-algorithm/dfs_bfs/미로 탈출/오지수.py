from collections import deque

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

count = 0
queue = deque([[0, 0]])
visited[0][0] = True

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

while queue:
    i, j = queue.popleft()

    for di, dj in direction:
        if 0 <= i + di <= n - 1 and 0 <= j + dj <= m - 1 \
                and maze[i + di][j + dj] and not visited[i + di][j + dj]:
            queue.append([i + di, j + dj])
            maze[i + di][j + dj] = maze[i][j] + 1
            visited[i + di][j + dj] = True

# maze 출력 확인
# for i in range(n):
#     for j in range(m):
#         print(maze[i][j], end=" ")
#     print()
# print()

print(maze[n - 1][m - 1])
