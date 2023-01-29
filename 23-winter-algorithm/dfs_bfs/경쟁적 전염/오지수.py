from collections import deque

n, k = map(int, input().split())
virus = []
graph = []
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        if graph[i][j]:
            virus.append([graph[i][j], i, j])
time, x, y = map(int, input().split())
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
virus.sort()
virus = deque(virus)

cnt = 0
prev_num = 1
while virus:
    num, start_row, start_col = virus.popleft()
    if prev_num == k and num == 1:
        cnt += 1
    if time == cnt: # time check
        break
    for d_row, d_col in direction:
        next_row, next_col = start_row + d_row, start_col + d_col
        if 0 <= next_row < n and 0 <= next_col < n and \
                not graph[next_row][next_col]:
            graph[next_row][next_col] = num
            virus.append([num, next_row, next_col])
    prev_num = num

# print(graph)  # test
print(graph[x - 1][y - 1])
