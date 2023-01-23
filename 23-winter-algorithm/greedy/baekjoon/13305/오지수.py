'''
도시를 이동할때 1km 당 1L의 기름 사용함
원안의 숫자 - 주유소의 리터당 가격

-input
도시의 개수 n
도로의 길이 n-1개의 자연수
주유소의 리터당 가격 왼쪽 도시부터 n개의 자연수

-output
최소비용 출력
'''

n = int(input())
roads = list(map(int, input().split()))
oils = list(map(int, input().split()))

result = 0
cheap = oils[0]

for i in range(n-1):
    if oils[i] < cheap:
        cheap = oils[i]
    result += (roads[i] * cheap)

print(result)