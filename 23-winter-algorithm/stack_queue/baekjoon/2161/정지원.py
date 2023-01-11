from collections import deque

N = int(input())
list = deque(list(range(1, N+1)))
a = []
for i in range(N):
    a.append(str(list.popleft()))
    print(deque.rotate(list, -1))


