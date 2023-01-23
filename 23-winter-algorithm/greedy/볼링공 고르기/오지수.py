'''
- iput
n = 볼링공의 개수, m = 공의 최대 무게
각 볼링공의 무게 k
'''

# 처음 풀이
n, m = map(int, input().split())
balls = list(map(int, input().split()))
count = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if balls[i] != balls[j]:
            count += 1

print(count)

# 이중 반복문 사용하지 않은 풀이

n, m = map(int, input().split())
balls = list(map(int, input().split()))
weights = [0] * 10
count = 0  # 경우의 수
total = 0  # 무게를 기준으로 개수를 저장했을 때, 지금까지 나온 공의 수

for b in balls:  # 각 무게 당 리스트
    weights[b - 1] += 1

for w in weights:
    count += total * w  # total * 현재 공의 수
    total += w

print(count)
