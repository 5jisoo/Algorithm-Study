n, m = map(int, input().split())
tteok = list(map(int, input().split()))
h = 0
cut = []

left = 0
right = max(tteok)
while left <= right:
    mid = (left + right) // 2
    h = mid
    for i in range(n):
        if tteok[i] > h:
            cut.append(tteok[i] - h)
        else:
            cut.append(0)
    if sum(cut) > m:
        left = mid + 1
    else:
        right = mid - 1
    cut = []

print(h)