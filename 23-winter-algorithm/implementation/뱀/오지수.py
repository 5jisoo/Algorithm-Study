n = int(input())  # 보드의 크기
k = int(input())  # 사과의 개수

board = [[0] * n for _ in range(n)]  # 보드 생성

# 사과의 위치 (행, 열)
for _ in range(k):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1  # 1이 있는 곳 - 사과

l = int(input())  # 방향 변환 횟수

time_dir = []  # [시간, 방향] 저장
for _ in range(l):  # x초 후 c방향으로 전환 (c방향 :: L - 왼쪽, D - 오른쪽)
    x, c = input().split()
    x = int(x)
    time_dir.append([x, c])

# game start
head_r, head_c = 0, 0  # 머리 위치
tail_r, tail_c = 0, 0  # 꼬리 위치

board[head_r][head_c] = 2  # 기본 뱀 위치 표시
snake = [[head_r, head_c]]  # 첫번째 원소가 꼬리 위치

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 이동 방향들
dir_idx = 0  # 오른쪽으로 이동하면 dir_idx += 1, 왼쪽 dir_idx -= 1

change_cnt = 0  # n번째 변환

# 기본 보드 확인
# for i in range(n):
#     for j in range(n):
#         print(board[i][j], end=" ")
#     print()
# print()

time = 0
while True:
    time += 1

    # 머리 이동
    head_r += direction[dir_idx][0]
    head_c += direction[dir_idx][1]

    # 벽 확인
    if head_r >= n or head_c >= n or head_r < 0 or head_c < 0:  # 부딪히면 게임 종료
        print(time)
        exit(0)

    # 다른 몸 확인
    if board[head_r][head_c] == 2:  # board에 2로 표시되어 있으면 몸에 부딪힌 것.
        print(time)
        exit(0)

    if board[head_r][head_c] != 1:  # 머리 위치에 사과 없음
        tail_r, tail_c = snake.pop(0)
        board[tail_r][tail_c] = 0  # 꼬리 짧아짐.

    board[head_r][head_c] = 2  # 머리 이동 표시
    snake.append([head_r, head_c])  # 뱀 위치 표시

    # 변환 확인
    if change_cnt < l and time == time_dir[change_cnt][0]:
        if time_dir[change_cnt][1] == "D":
            dir_idx = (dir_idx + 1) % 4  # 오른쪽
        else:
            dir_idx = (dir_idx - 1 + 4) % 4  # 왼쪽
        change_cnt += 1

    # 보드 프린트용
    # for i in range(n):
    #     for j in range(n):
    #         print(board[i][j], end=" ")
    #     print()
    # print()
