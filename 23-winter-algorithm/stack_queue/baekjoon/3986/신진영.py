# 짝 지어 없애는 것 -> stack 생각
# 처음: list로 저장한 다음에 그 안에서 비교 하려고 함->꼭 저장할필요 X, 이 문제처럼 stack 이용하면 더 간단
from sys import stdin

N = int(stdin.readline())
good = 0

def good_word(s):
  str = []
  for i in range(len(s)):
    # or 뒤 조건을 먼저 쓰면 indexOutOfRange발생 주의(or의 특징)
    if len(str) == 0 or str[-1] != s[i]: 
      str.append(s[i])
    else:
      str.pop()
  return True if len(str) == 0 else False

for i in range(N):
  word = stdin.readline().strip()
  if good_word(word): good += 1

print(good)

