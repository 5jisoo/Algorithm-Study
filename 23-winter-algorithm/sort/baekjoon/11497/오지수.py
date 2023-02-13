test_case = int(input())
for _ in range(test_case):
    num = int(input())
    log_list = list(map(int, input().split()))
    log_list.sort()

    array = [0] * num

    left_idx = 0
    right_idx = num - 1
    for i in range(num):
        if i % 2 == 0:
            array[left_idx] = log_list[i]
            left_idx += 1
        else:
            array[right_idx] = log_list[i]
            right_idx -= 1
    array.append(log_list[0])

    max_result = 0
    for i in range(num):
        max_result = max(abs(array[i+1] - array[i]), max_result)

    print(max_result)
