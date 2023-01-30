from collections import deque

# 입력
n, m, v = map(int, input().split())
# 노드번호가 1부터인것을 고려해서 애초에 n+1 * n+1 입력받음 => 이렇게 해야만 하나? 이게 간단해서 그런듯
graph = [[0] * (n+1) for i in range(n+1)]
# 인접행렬 입력받기
for _ in range(m):
  tn, tm = map(int, input().split())
  graph[tn][tm] = 1
  graph[tm][tn] = 1
# 방문여부 배열
visited = [False] * (n+1)

# dfs 함수 정의
def dfs(g, v):
  # 방문한 노드임을 표시하고 출력
  global visited
  visited[v] = True
  print(v, end=' ')
  # 방문하지 않은 노드 찾기
  for i in range(1, n+1):
    # 간선이 존재하면 g[v]리스트에서 1 이니까 조건으로 걸기
    if not visited[i] and g[v][i]:
      dfs(g, i)

# bfs 함수 정의
def bfs(g, v):
  global visited
  visited = [False] * (n+1)
  visited[v] = True
  queue = deque([v])

  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in range(1,n+1):
      if not visited[i] and g[v][i]:
        queue.append(i)
        visited[i] = True

dfs(graph, v)
print()
bfs(graph, v)