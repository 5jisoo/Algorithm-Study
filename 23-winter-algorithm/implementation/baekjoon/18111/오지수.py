import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
max_value = 0
min_value = 500
for i in range(n):
    data = list(map(int, input().split()))
    ground.append(data)
    max_value = max(max_value, max(data))
    min_value = min(min_value, min(data))

result_time = 1e9
result_height = 0
for height in range(257):  # 맞출 높이
    cnt_high = 0
    cnt_low = 0
    for i in ground:
        for j in i:
            if j > height:  # 맞출 높이 보다 땅이 높은 경우
                cnt_high += (j - height)
            else:  # 맞출 높이 보다 땅이 낮을 경우
                cnt_low += (height - j)
    inven = cnt_high + b
    if inven < cnt_low:  # 만약 인벤토리가 부족했다면 그냥 skip
        continue
    time = 2 * cnt_high + cnt_low
    if time <= result_time:
        result_time = time
        result_height = height
print(result_time, result_height)
