# while문에서 똑같은 조건을 반복했다가 개선
from sys import stdin

N = int(stdin.readline())

cards = []
for i in range(N):
  cards.append(i+1)

away = []

while True:
  first = cards.pop(0)
  away.append(first)
  if len(cards) == 0:
    break
  second = cards.pop(0)
  cards.append(second)

for i in away:
  print(i, end=" ")