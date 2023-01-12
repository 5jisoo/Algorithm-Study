'''
n= 모험가의 수
각 모험도의 공포도의 값
'''

n = int(input())
count = 0
fears = list(map(int, input().split()))
fears.sort()

grp = 0  # 현재 만들어지고 있는 group의 인원수 count.

for f in fears:
    grp += 1
    if f <= grp:
        count += 1  # 그룹 하나 완성
        grp = 0  # 새로운 그룹 모집 시작

print(count)