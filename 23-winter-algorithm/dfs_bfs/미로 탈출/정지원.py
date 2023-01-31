#가까운 노드를 확인하여 1인 노드면 최단경로 값을 +1해야하므로 가까운 노드부터 차례로 탐색하는 BFS를 이용해야함.
#그래프를 벗어나거나 사이드에 도달하면 아무일도 일어나지 않게 해야함
from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int(input()))))

#좌표 x,y이동값 리스트로 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue #공간 벗어났을때 아무일도 안일어나게 하는거 루프 종료로 해버리면 진행이 안되므로 continue로 해야함.
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))

