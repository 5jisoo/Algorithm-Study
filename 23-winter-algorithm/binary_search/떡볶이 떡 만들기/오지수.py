n, m = map(int, input().split())
tteok_list = list(map(int, input().split()))

start = 0
end = max(tteok_list)

answer = 0
while start <= end:
    height = (start + end) // 2
    result = 0
    for tteok in tteok_list:
        if tteok > height:
            result += (tteok - height)
    if result < m:
        end = height - 1
    else:
        answer = height
        start = height + 1
print(answer)