tmp = input()
x, y = tmp[0], tmp[1]

# 알파벳 -> 좌표 변환
# 앞으론 ord() 활용하자 !
tmp_dict = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8 }
# 상하좌우(4)*2 = 8가지의 이동에 따른 x, y 좌표
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]
cnt = 0

# 각 경우마다 좌표평면 안에 있는지 확인
# 최대 경우의 수는 8
for i in range(8):
  next_x, next_y = tmp_dict[x], int(y)
  next_x += dx[i]
  next_y += dy[i]
  if next_x < 1 or next_y > 8 or next_y < 1 or next_y > 8: continue
  else: cnt += 1 # 이렇게 or 그냥 여사건일때 -> cnt +1로 구현해도 됨

print(cnt)