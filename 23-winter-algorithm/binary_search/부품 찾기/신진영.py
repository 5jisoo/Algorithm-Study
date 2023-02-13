def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

for num in want:
    if bin_search(have, num, 0, n-1) == -1:
        print("no", end=" ")
    else:
        print("yes", end=" ")