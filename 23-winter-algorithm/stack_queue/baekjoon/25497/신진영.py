# 문제의 설명 부족. 잘못사용된 기술 있으면 그 이후 count X
from sys import stdin

N = int(stdin.readline())
skill = stdin.readline().strip()
cnt = 0
Lstack = []
Sstack = []

for i in skill:
  if i == 'L':
    Lstack.append('L')
  elif i == 'R':
    if Lstack:
      cnt += 1
      Lstack.pop()
    else: break
  elif i == 'S':
    Sstack.append('S')
  elif i == 'K':
    if Sstack:
      cnt += 1
      Sstack.pop()
    else: break
  else: cnt += 1

print(cnt)