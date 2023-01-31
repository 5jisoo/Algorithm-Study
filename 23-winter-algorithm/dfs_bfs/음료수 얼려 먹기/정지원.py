#노드가 0인지 1인지를 확인하고 0일때 주변 상하좌우 노드들도 0인지를 확인해야하므로 재귀함수(DFS)를 이용해야함.
n,m = map(int(input().split()))

graph = []
for i in range(n):
    graph.append(list(map(int,input()))) #행이 n개인 2차원 리스트맵

def dfs(x,y):
    if x<= -1 or x >= n or y <= -1 or y >=m:
        return False #종료되는 경우의 코드를 꼭 짜줘야함
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False # Q.여기서 굳이 else 안쓰고 넘어가도 되는건가?

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
        
print(result)

