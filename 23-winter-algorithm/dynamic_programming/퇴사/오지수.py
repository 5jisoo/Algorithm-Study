n = int(input())
d = [0] * n
data = []
max_data = (0,0)
for _ in range(n):
    t, p = map(int, input().split())
    data.append((t, p))

for i in range(n-1, -1, -1):
    if i + data[i][0] <= n:
        d[i] = data[i][1]
    if i + data[i][0] < n:
        d[i] += max(d[i + data[i][0]:])

d.sort(reverse=True)
print(d[0])