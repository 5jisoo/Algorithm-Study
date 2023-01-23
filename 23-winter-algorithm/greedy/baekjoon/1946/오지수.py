import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    for __ in range(n):
        doc, itv = map(int, input().split())
        data.append((doc, itv))
    data.sort()
    result = n
    check_i = data[0][1]
    for (d, i) in data:
        if i > check_i:
            result -= 1
        else:
            check_i = i
    print(result)