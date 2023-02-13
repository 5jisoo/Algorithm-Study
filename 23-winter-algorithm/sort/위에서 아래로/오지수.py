n = int(input())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

for d in data:
    print(d, end=" ")
