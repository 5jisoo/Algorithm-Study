from collections import deque

n, m, distance, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)  # 방문 여부 + 거리 저장

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()

count = 0
queue = deque([start])
visited[start] = 1
while queue:
    start = queue.popleft()
    for next_city in graph[start]:
        if not visited[next_city]:
            queue.append(next_city)
            visited[next_city] = visited[start] + 1

check = 0
for i in range(len(visited)):
    if visited[i] - 1 == distance:
        check = 1
        print(i)

if not check:
    print("-1")