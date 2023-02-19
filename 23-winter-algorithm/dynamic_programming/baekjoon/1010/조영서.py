import math

t = int(input())
answer = []
for _ in range(t):
    n,m = map(int, input().split())
    count = math.factorial(m) // (math.factorial(n)*math.factorial(m-n))
    answer.append(count)

for i in range(len(answer)):
    print(answer[i])




