n, x = map(int, input().split())
num_list = list(map(int, input().split()))

'''
# 시간복잡도 높게 나올것 같아서 다시 풀었음.

def binary_search(start, end):
    answer = 0
    if start > end:
        return 0
    mid = (start + end) // 2
    if num_list[mid] == x:
        answer += 1
        answer += binary_search(mid + 1, end)
        answer += binary_search(start, mid - 1)
    elif num_list[mid] > x:
        answer += binary_search(start, mid - 1)
    else:
        answer += binary_search(mid + 1, end)
    return answer
'''


def binary_search(array, x):
    length = len(array)

    a = first(array, x, 0, length - 1)

    if a == None:
        return 0
    b = last(array, x, 0, length - 1)

    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


count = binary_search(num_list, x)

if count:
    print(count)
else:
    print(-1)
