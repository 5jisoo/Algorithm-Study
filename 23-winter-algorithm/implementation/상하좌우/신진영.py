N = int(input()) # 공간의 크기
move = input().split() # 이동계획 입력받기

x,y = 1,1 # 처음위치
# U, D, L, R에 따라 이동
for m in move:
  if m == "U" and (x-1) >= 1:
    x -= 1
  elif m == "D" and (x+1) <= N:
    x += 1
  elif  m == "L" and (y-1) >= 1:
    y -= 1
  elif m == "R" and (y+1) <= N:
    y += 1

print(x,y)