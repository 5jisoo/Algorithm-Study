import sys
import heapq

# 정렬상태를 유지해야하므로 우선순위 큐 사용

input = sys.stdin.readline

n = int(input())
lecs = []
rooms = []

for _ in range(n):
    start, end = map(int, input().split())
    lecs.append((start, end))

lecs.sort()
rooms.append(lecs[0][1])

for (s, e) in lecs[1:]:
    if s < rooms[0]:
        heapq.heappush(rooms, e)
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, e)

print(len(rooms))