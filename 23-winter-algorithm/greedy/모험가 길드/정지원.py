N = int(input())
data = list(map(int, input().split()))
data.sort()#여기까지만 혼자 적음. 밑부터는 코드 읽으면서 이해함.처음에 가장 큰 수 기준으로 그룹을 짜야한다 생각했는데 방향을 잘못 잡음. '최소한의 사람 수 = 최대한 많은 그룹' 

group = 0
person = 0

for i in data:
    person += 1
    if person >= i:
        group += 1
        person = 0

print(group)

