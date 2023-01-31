import heapq

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
heapq.heapify(data)

if n == 1:
    print(0)
    exit(0)

time = 0
while data:
    first = heapq.heappop(data)
    if not data:
        break
    sec = heapq.heappop(data)
    time += (first + sec)
    heapq.heappush(data, first + sec)

print(time)