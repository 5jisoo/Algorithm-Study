n = int(input())

data = []
for _ in range(n):
    name, score = input().split()
    data.append([name, int(score)])

data.sort(key=lambda x: x[1])   # 점수 기준으로 정렬

for name, score in data:
    print(name, end=" ")
