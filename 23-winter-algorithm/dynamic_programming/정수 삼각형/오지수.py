n = int(input())
d = [[0] * i for i in range(1, n + 1)]
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i + 1):
        if i == 0:
            d[i][j] = data[i][j]
            continue

        # 왼쪽 위 부모 탐색
        if j - 1 >= 0:
            d[i][j] = max(d[i][j], data[i][j] + d[i - 1][j - 1])

        # 오른쪽 위 부모 탐색
        if j <= i - 1:
            d[i][j] = max(d[i][j], data[i][j] + d[i - 1][j])

print(max(d[-1]))
