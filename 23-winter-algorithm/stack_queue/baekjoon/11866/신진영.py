# 인덱스 에러 남 ㅡㅡ
from sys import stdin

N, K = map(int,stdin.readline().split())
n = N
ppl = []
yose = []

ppl = [i+1 for i in range(N)]

idx = -1
while n:
  idx = (idx + K) % n
  num = ppl.pop(idx)
  idx -= 1
  yose.append(num)
  n -= 1

print("<", end="")
for j in range(N):
  if j == (N-1):
    print(str(yose[j])+">")
    break
  print(str(yose[j])+",", end=" ")