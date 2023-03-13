k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

while(start <= end):
    mid = (start + end) // 2
    div = 0
    for num in arr:
        div += (num // mid)

    if div < n:
        end = mid - 1
    else:
        start = mid + 1
        
print(end)