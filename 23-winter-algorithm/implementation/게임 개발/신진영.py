n, m = map(int, input().split()) # map size
x, y, view = map(int, input().split()) # position, view
map_lst = []
ways = []
# 처음 위치 추가
ways.append((x, y))
check_count = 0

# input map
for i in range(n):
  map_lst.append(list(map(int, input().split())))

# escape condition: check 4position but can't move, can't move 1 back
# 현재 방향 기준으로 왼쪽방향 탐색
while True:
  if view == 0:
    tx, ty = x-1, y
  elif view == 1:
    tx, ty = x, y-1
  elif view == 2:
    tx, ty = x+1, y
  elif view == 3:
    tx, ty = x, y+1

  # 모든 조건 만족하면 이동
  # 좌표가 맵 내에 있고, 이동할 위치가 육지이고, 방문한 위치가 아닐 때
  if 0 <= tx < n and 0 <= ty < m and  map_lst[tx][ty] == 0 and (tx, ty) not in ways:
    x = tx
    y = ty
    ways.append((tx, ty)) # 이동한 위치 기록
    check_count = 0
  elif check_count < 3: # 아직 모든 방향 탐색 이전이라면 다음방향 확인위해 view변경
    check_count += 1
    view += 1
    view %= 4
    continue
  elif check_count == 3: # 모든 방향 탐색하고도 이동하지 못했다면 기존방향대로 뒤로 한 칸 이동
      view += 1
      view %= 4
      if view == 0:
        tx, ty = x, y+1
      elif view == 1:
        tx, ty = x-1, y
      elif view == 2:
        tx, ty = x, y-1
      elif view == 3:
        tx, ty = x+1, y
      
      if map_lst[tx][ty] == 1: # 뒤쪽 방향이 바다라면 break
        break
      else: # 뒤로 이동할 수 있다면 이동
        x = tx
        y = ty
        check_count = 0
print(len(ways))
