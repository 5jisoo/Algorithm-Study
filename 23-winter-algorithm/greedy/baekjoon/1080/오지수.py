import sys

input = sys.stdin.readline


def change(i, j):
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            a[k][l] ^= 1


n, m = map(int, input().split())
a = []
b = []
count = 0
for _ in range(n):
    a.append(list(map(int, input().strip())))
for _ in range(n):
    b.append(list(map(int, input().strip())))

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            if i + 2 >= n or j + 2 >= m:
                print("-1")
                exit(0)
            change(i, j)
            count += 1

print(count)