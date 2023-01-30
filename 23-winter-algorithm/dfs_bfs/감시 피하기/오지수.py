from itertools import combinations

n = int(input())
data = []
wall = []
teacher = []
for i in range(n):
    new = input().strip().split()
    data.append(new)
    for j in range(n):
        if data[i][j] == "X":
            wall.append([i, j])
        elif data[i][j] == "T":
            teacher.append([i, j])

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def check(data):
    for t_row, t_col in teacher:
        for d_row, d_col in direction:
            next_row, next_col = t_row + d_row, t_col + d_col
            while 0 <= next_row < n and 0 <= next_col < n:
                if data[next_row][next_col] == "S":
                    return False
                elif data[next_row][next_col] == "O":
                    break
                next_row += d_row
                next_col += d_col
    return True

wall = list(combinations(wall, 3))
for w in wall:
    for i, j in w:
        data[i][j] = "O"
    if check(data):
        print("YES")
        exit(0)
    for i, j in w:
        data[i][j] = "X"

print("NO")