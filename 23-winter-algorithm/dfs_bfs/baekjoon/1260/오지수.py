from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for g in graph:  # 가장 작은 원소부터
    g.sort()


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    print(start, end=" ")
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i, end=" ")


dfs(graph, v, visited)
print()
visited = [False] * (n + 1)  # 방문 여부 초기화
bfs(graph, v, visited)