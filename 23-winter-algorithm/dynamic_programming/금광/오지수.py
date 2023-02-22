test = int(input())

for _ in range(test):
    n, m = map(int, input().split())
    d = [[0] * m for _ in range(n)]
    input_data = list(map(int, input().split()))
    data = [[input_data[j + i * m] for j in range(m)] for i in range(n)]

    for j in range(m):
        for i in range(n):
            if j == 0:
                d[i][j] = data[i][j]
                continue
            # 왼쪽 위 확인
            if i - 1 >= 0 and j - 1 >= 0:
                d[i][j] = max(d[i][j], data[i][j] + d[i - 1][j - 1])
            # 왼쪽 확인
            if j - 1 >= 0:
                d[i][j] = max(d[i][j], data[i][j] + d[i][j - 1])
            # 왼쪽 아래 확인
            if i + 1 < n and j - 1 >= 0:
                d[i][j] = max(d[i][j], data[i][j] + d[i + 1][j - 1])
    print(max([d[i][-1] for i in range(n)]))
