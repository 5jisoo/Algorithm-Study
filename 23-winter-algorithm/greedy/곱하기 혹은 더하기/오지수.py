# 삼항 연산자 사용
data = list(map(int, input()))
num = data[0]

for d in data[1:]:  # 더한 결과와 곱한 결과 비교
    num = num + d if num + d >= num * d else num * d

print(num)


'''
# 다른 방법!


data = list(map(int, input()))
num = data[0]

for d in data[1:]:
    if d <= 1 or num <= 1:  # 둘중에 하나만 0 또는 1이면 무조건 더해주면 됨
        num += d
    else:
        num *= d

print(num)

'''
