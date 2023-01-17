n, m = map(int, input().split())
row, col, dir = map(int, input().split())

map_list = []
check_list = [[0] * m for _ in range(n)]
dir_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 순서대로 북, 동, 남, 서 - dir을 인덱스로 사용하여 좌표 가져올 수 있음.

for i in range(n):
    map_list.append(list(map(int, input().split())))

result = 1
check_list[row][col] = 1  # 현재 좌표 방문처리
count = 0  # 네 방향 체크

while True:
    count += 1
    dir = (dir + 3) % 4  # turn left
    next_row = dir_list[dir][0] + row
    next_col = dir_list[dir][1] + col
    if map_list[next_row][next_col] == 0 and check_list[next_row][next_col] == 0:
        row = next_row
        col = next_col
        check_list[next_row][next_col] = 1
        result += 1
        count = 0
    if count == 4:  # 네 방향 모두 체크한 경우
        row -= dir_list[dir][0]
        col -= dir_list[dir][1]
        count = 0
        if map_list[row][col] == 1:
            break

print(result)
