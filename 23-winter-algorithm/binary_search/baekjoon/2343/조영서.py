import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lec = list(map(int, input().split()))

left = max(lec)
right = sum(lec)

while (left <= right):
    blue = (left+right) // 2
    total = 0
    count = 1
    for i in range(n):
        if (total+lec[i] > blue):
            count += 1
            total = 0
        total += lec[i]
        if (count > m):
            break
    if (count > m):
        left += 1
    else:
        right -= 1

print(left)
