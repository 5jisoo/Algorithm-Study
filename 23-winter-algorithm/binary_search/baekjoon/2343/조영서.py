import sys
input = sys.stdin.readline

n,m = map(int, input().split())
online = [int(input()) for _ in range(n)]

left, right =1, max(online)

while (left <= right):
    size = (left+right) // 2
    count = 0
    for i in online:
        count += i // size
        if (count > m):
            break
    if (count >= m):
        left = size + 1
    else:
        right = size - 1

print(right)