N = 1260
coins = [500, 100, 50, 10]
count = 0   # 코인의 개수

for coin in coins:
    count += N // coin
    N %= coin

print(count)