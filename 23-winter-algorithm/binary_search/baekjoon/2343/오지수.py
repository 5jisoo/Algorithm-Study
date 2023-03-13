n, m = map(int, input().split())
lectures = list(map(int, input().split()))

start = max(lectures)
end = sum(lectures)

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    temp = 0
    for lecture in lectures:
        temp += lecture
        if temp == mid:
            cnt += 1
            temp = 0
        elif temp > mid:
            cnt += 1
            temp = lecture
    if temp: cnt += 1
    if cnt > m:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
print(result)
