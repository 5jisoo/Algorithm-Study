#문제 이해부터가 너무 어려웠음...고민하는데 1시간, 다른 사람들 코드 서치하고 이해하는데 1시간 쫌 넘게 걸렸는데 이게 맞나..
from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        for now, dist in graph[node]:
            if not visited[now]:
                dist[now] = dist[node]+dist
                queue.append(now)
                visited[now] = True   
    return graph

n,m,k,x = map(int, input().split())
graph = [[] for _ in range n+1] # Q.처음에 행이 n개인 그래프를 만들어야한다고 생각했는데 왜 n+1로 잡아야하는거지..?일단 풀고 교재 확인해보니 n+1로 잡았길래 수정해놨는데 이유 아는사람 답변 달아주면 좋겠다

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))#여기까진 막힘없이 짰는데 이후 코드를 짜는데 헤맴

visited = [False] * (n+1)
dist = [0] * (n+1)

bfs(graph, x, visited)

answer = []
for idx, distance in enumerate(dist): 
    #enumerate()내장함수는 원소와 원소의 인덱스를 함께 출력함. 
    # list = [100,200,300]
    # for i in enumerate(list):
    #    print(i) => (0,100) (1,200) (3,300) 의 형태로 인덱스와 리스트의 원소 순서로 출력됨
    if distance == k:
        answer.append(idx)
    if not answer:
        print(-1)
    else:
        answer.sort()
        for ans in answer:
            print(ans)


