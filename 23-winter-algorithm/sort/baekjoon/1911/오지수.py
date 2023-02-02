n, l = map(int, input().split())
pool_list = []
for _ in range(n):
    start, end = map(int, input().split())
    pool_list.append((start, end))

pool_list.sort()

''' 
통과한 소스코드지만, 시간 단축을 위해 다시 풀었음.

result = 0
current_pool = 0  # 현재 덮고 있는 웅덩이 idx
plank = 0  # 현재 널빤지가 시작할 위치
while current_pool <= (n - 1):
    if pool_list[current_pool][0] <= plank < pool_list[current_pool][1]:
        result += 1
        plank += l
    if current_pool < (n - 1) and pool_list[current_pool][1] <= plank < pool_list[current_pool + 1][0]:
        current_pool += 1
        plank = pool_list[current_pool][0]
    if current_pool < (n - 1) and plank >= pool_list[current_pool + 1][0]:
        current_pool += 1
    if plank >= pool_list[-1][1]:
        break
print(result)

'''

result = 0
plank = 0  # 현재 널빤지가 시작할 위치
for start, end in pool_list:
    if plank > end:
        continue

    if plank < start:
        plank = start

    diff = end - plank
    remain = 1
    if diff % l == 0:  # 현재 덮고 있는 웅덩이가 널빤지 길이에 딱 맞아떨어지는 경우
        remain = 0
    cnt = (diff // l + remain)  # 덮을 널빤지의 개수
    plank += cnt * l  # 널빤지 이동
    result += cnt
print(result)
