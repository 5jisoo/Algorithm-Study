test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    count = 0  # count = 출력 순서
    docs_que = list(map(int, input().strip().split()))
    while docs_que:
        if docs_que[0] >= max(docs_que):
            docs_que.pop(0)
            n -= 1
            count += 1
            if m == 0:
                break
        else:
            docs_que.append(docs_que.pop(0))
        m = (m - 1) % n
    print(count)