crd = list(input())
crd[0], crd[1] = int(ord(crd[0]) - ord("a") + 1), int(crd[1])

# 나올 수 있는 이동방향의 경우의 수
dirs = [[-1, 2], [1, 2], [2, -1], [2, 1], [-2, -1], [-2, 1], [1, -2], [-1, -2]]

cnt = 0
for x, y in dirs:
    if 1 <= crd[0] + x <= 8 and 1 <= crd[1] + y <= 8:
        cnt += 1

print(cnt)
