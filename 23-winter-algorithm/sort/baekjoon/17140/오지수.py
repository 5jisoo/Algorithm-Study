r, c, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(3)]


def cal_r():
    global a
    new_graph = []

    for row in a:
        row.sort()
        new_row = []

        nums = set(row)  # 숫자들만 담은 집합
        for num in nums:
            if num == 0:
                continue
            new_row.append([num, row.count(num)])
        new_row.sort(key=lambda x: (x[1], x[0]))
        new_row = sum(new_row, [])  # 새로운 표현 기억하기 - 여러 리스트를 하나의 리스트로 합치기
        new_graph.append(new_row[:100])  # 100개 제한

    max_cnt = max(map(len, new_graph))  # 최대 길이 - 표현 기억하기

    for row in new_graph:  # 부족한 길이 0으로 맞춰주기
        if len(row) < max_cnt:
            row.extend([0] * (max_cnt - len(row)))
    a = new_graph


result = 0
flag = 0
while result <= 100:
    try:  
        if a[r - 1][c - 1] == k:
            print(result)
            flag = 1
            break
    except:
        pass # 표현 기억하기

    if len(a[0]) > len(a):
        a = list(map(list, zip(*a)))  # 표현 기억하기
        cal_r()
        a = list(map(list, zip(*a)))
    else:
        cal_r()
    result += 1

if not flag:
    print(-1)
