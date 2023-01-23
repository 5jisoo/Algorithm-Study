from collections import deque

n, k = map(int, input().split())
d = deque([i for i in range(1, n+1)])
list = []

while d:
    d.rotate(-(k-1))
    list.append(d.popleft())

print('<', end = '')
for i in range(len(list)):
    if i != len(list)-1:
        print("%d, " %list[i], end = '')
    else:
        print("%d>" %list[i])
