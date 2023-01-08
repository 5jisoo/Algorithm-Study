# 인덱스 에러 남 ㅡㅡ
from sys import stdin

N, K = map(int,stdin.readline().split())
ppl = []
yose = []

for i in range(N):
  ppl.append(i+1)

idx = -1
while len(ppl) > 0:
  if len(ppl) == 1:
    yose.append(ppl[0])
    break
  idx += K
  if idx > len(ppl):
    idx %= len(ppl)
  num = ppl.pop(idx)
  idx -= 1
  yose.append(num)


print("<", end="")
for j in range(N):
  if j == (N-1):
    print(str(yose[j])+">")
    break
  print(str(yose[j])+",", end=" ")