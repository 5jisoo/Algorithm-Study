n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 0
end = max(tree_list)

result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for tree in tree_list:
        if tree > mid:
            count += (tree - mid)

    if count < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)