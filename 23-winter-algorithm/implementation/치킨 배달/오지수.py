from itertools import *

n, m = map(int, input().split())

cks = []
house = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append((i, j))
        elif data[j] == 2:
            cks.append((i, j))

result = list(combinations(cks, m))

total_cnt = 1e9  # 가장 작은 도시 치킨 거리
for r in result:
    cnt = 0  # result의 각 조합에서 나온 도시 치킨 거리
    for row, col in house:  # 집
        tmp = 1e9  # 집과 치킨집 사이 가장 가까운 거리
        for x, y in r:  # 치킨집들
            tmp = min(tmp, abs(x - row) + abs(y - col))
        cnt += tmp
    total_cnt = min(cnt, total_cnt)
print(total_cnt)
