n, c = map(int, input().split())
house_list = []
for i in range(n):
    house_list.append(int(input()))
house_list.sort()

start = 1
end = max(house_list)

result = 0
while start <= end:
    max_dist = (start + end) // 2
    cnt = 0
    temp = 0
    for i in range(len(house_list) - 1):
        temp += (house_list[i + 1] - house_list[i])
        if temp >= max_dist:
            cnt += 1
            temp = 0
    if cnt + 1 < c:
        end = max_dist - 1
    else:
        result = max_dist
        start = max_dist + 1

print(result)