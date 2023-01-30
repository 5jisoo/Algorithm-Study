'''
놓친 부분: 하루에 연합이 !!여러개!! 생길 수 있다는 점을 고려해야 함.
테스트 케이스를 돌려볼 때 코드가 틀려서 놓친 부분을 확인하느라 시간이 오래 걸림.
'''

from collections import deque

n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

count = 0
while True:
    check = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                allies = [[i, j]]
                visited[i][j] = True
                queue = deque(allies)
                while queue:
                    start_row, start_col = queue.popleft()
                    for d_row, d_col in direction:
                        next_row, next_col = start_row + d_row, start_col + d_col
                        if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col] and \
                                l <= abs(people[start_row][start_col] - people[next_row][next_col]) <= r:
                            allies.append([next_row, next_col])
                            queue.append([next_row, next_col])
                            visited[next_row][next_col] = True
                if len(allies) >= 2:
                    sum_value = 0
                    check = 1
                    for row, col in allies:
                        sum_value += people[row][col]
                    aver = sum_value // len(allies)
                    for row, col in allies:
                        people[row][col] = aver
    if not check:
        break
    else:
        count += 1

print(count)
