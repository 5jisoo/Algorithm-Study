n = int(input())
numbers = list(map(int, input().split()))

start_idx = 0
end_idx = n - 1

while start_idx <= end_idx:
    mid_idx = (start_idx + end_idx) // 2
    if mid_idx == numbers[mid_idx]:
        print(mid_idx)
        exit(0)
    elif mid_idx < numbers[mid_idx]:
        end_idx = mid_idx - 1
    else:
        start_idx = mid_idx + 1

print(-1)