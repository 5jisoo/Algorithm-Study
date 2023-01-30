'''
이런식으로 애초에 row, col 좌표값을 따로 저장하는 변수로 계산함.
'''

n = int(input())
moves = input().split()
row, col = 1, 1

for m in moves:
    if m == "L" and col >= 1:
        col -= 1
    elif m == "R" and col <= n:
        col += 1
    elif m == "U" and row >= 1:
        row -= 1
    elif m == "D" and row <= n:
        row += 1

print(row, col)
