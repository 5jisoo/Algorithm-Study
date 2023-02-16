n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [-1] * (max(coins) + 1)

for coin in coins:
    d[coin] = 1

for i in range(min(coins), m + 1):
    for coin in coins:
        if i - coin > 0 and d[i - coin] != -1:  # 만드는 방법 존재
            if d[i] == -1:  # 기존에 저장된 값이 없다면 - 저장
                d[i] = d[i - coin] + 1
            else:           # 있다면 - 비교 후 저장
                d[i] = min(d[i], d[i - coin] + 1)

print(d[m])
