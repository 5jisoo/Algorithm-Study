'''
사람 수 n
각 사람이 돈을 인출하는 시간 리스트

리스트를 정렬하여 작은 순서대로 더해주면 됨.
'''
n = int(input())
times = list(map(int, input().split()))
times.sort()

sum_value = 0
plus = 0
for t in times:
    plus += t
    sum_value += plus

print(sum_value)