def dfs(data, i, j):
    data[i][j] = 1
    direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]  # 동 서 남 북 방향
    for d_row, d_col in direction:
        # (순서대로) 범위내에 있으며, data가 0인지 확인
        if 0 <= i + d_row <= n - 1 and 0 <= j + d_col <= m - 1 \
                and not data[i + d_row][j + d_col]:
            dfs(data, i + d_row, j + d_col)  # 이동해서 다시 호출


n, m = map(int, input().split())

data = []
for _ in range(n):
    new = list(map(int, input()))
    data.append(new)

count = 0
for i in range(n):
    for j in range(m):
        if not data[i][j]:  # data가 0이라면 - 방문하지 않은 노드라면
            count += 1
            dfs(data, i, j)

print(count)
