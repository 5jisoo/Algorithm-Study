n = int(input())
food_list = list(map(int, input().split()))

d = [0] * (100 + 1)

d[0] = food_list[0]
d[1] = max(food_list[0], food_list[1])

for i in range(2, n):
    d[i] = max(food_list[i - 1], d[i - 2] + food_list[i])

print(d[n - 1])
