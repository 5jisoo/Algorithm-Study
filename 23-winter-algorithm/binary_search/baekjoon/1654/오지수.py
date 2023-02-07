k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))

start, end = 1, max(data)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in data:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)