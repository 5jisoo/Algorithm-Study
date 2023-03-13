# Q. 같은 지점에 집이 여러개 있는 경우엔 어떡하지..? -> 내린결론: 오름차순으로 나열하면 가운데 값 선택하는 덴 지장없음.
#사고과정: 4개의 지점을 오름차순으로 나열 후 가장 가운데 값 선택(인덱스 이용)
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(houses[(n-1)//2])