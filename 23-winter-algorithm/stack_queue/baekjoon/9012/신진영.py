# 3986과 똑같은 문제
# 지만 똑같이 푸니까 틀림
# 틀린이유: ()의 처음은 무조건 '(', 따라서')'가 처음으로 들어오는건 처리해줄 필요 없음
# flag 변수의 사용, 출력은 끝에 한번에

from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
  stack = []
  par = input().strip()
  isVPS = True # ())와 ()케이스의 구분을 위한 flag변수

  for i in par:
    if i == '(':
      stack.append(i)
    elif i == ')':
      if stack:
        stack.pop()
      else:
        isVPS = False
        break
  # if not stack and isVPS: 같은표현
  if len(stack) == 0 and isVPS:
    print("YES")
  elif len(stack) or not isVPS:
    print("NO")