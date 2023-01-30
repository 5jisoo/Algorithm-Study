n,m = map(int, input().split())
pattern = []
for i in range(n):
    pattern.append(list(input()))

count = 0
for i in range(n):
    for j in range(m):
        if pattern[i][j] == '-':
            if i == 1:
                continue
            elif (i == n-1) & (pattern[i][j] == pattern[i-1][j]):
                count += 1
            elif pattern[i][j] != pattern[i-1][j] :
                count += 1

for j in range(m):
    for i in range(n):
        if pattern[i][j] == 'ㅣ':
            if j == 1:
                continue
            elif (j == m-1) & (pattern[i][j] == pattern[i][j-1]):
                count += 1
            elif pattern[i][j] != pattern[i][j-1]:
                count += 1

print(count)