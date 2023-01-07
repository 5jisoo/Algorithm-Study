import sys

n,k = map(int, sys.stdin.readline().split())
p = [i for i in range(1,n+1)]
i = 0
print("<", end="")
while len(p)!= 0:
    i = (i + k - 1) % len(p)
    if len(p) == 1:
        print(p.pop(i), end="")
    else:
        print(p.pop(i), end=", ")
print(">")