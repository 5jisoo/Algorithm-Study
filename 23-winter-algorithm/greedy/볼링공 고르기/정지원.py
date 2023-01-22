N, M =map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
    array[x] += 1 #x가 무게고 array[x]에 해당하는 값이 그 무게의 볼링공의 개수라 생각하기

result = 0
for i in range(1, M+1):
    N -= array[i]
    result += array[i]*N

print(result)