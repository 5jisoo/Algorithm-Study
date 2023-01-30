import sys

n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
visited = [[False] * n for i in range(n)]

def jelly(x,y): #dfs
    if x >= n or y >= n:
        return False
    v = board[x][y]
    if visited[x][y]== False:
        visited[x][y] = True
        jelly(x+v, y)
        jelly(x, y+v)
        return True

jelly(0,0)
if visited[n-1][n-1]==True:
    print("HaruHaru")
else:
    print("Hing")
