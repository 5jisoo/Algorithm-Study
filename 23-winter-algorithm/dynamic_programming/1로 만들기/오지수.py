x = int(input())

num_list = [0] * 30001

for i in range(2, x + 1):
    num_list[i] = num_list[i - 1] + 1
    if i % 2 == 0:
        num_list[i] = min(num_list[i], num_list[i // 2] + 1)
    if i % 3 == 0:
        num_list[i] = min(num_list[i], num_list[i // 3] + 1)
    if i % 5 == 0:
        num_list[i] = min(num_list[i], num_list[i // 5] + 1)

print(num_list[x])
