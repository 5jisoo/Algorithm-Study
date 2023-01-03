## 두가지 방법 작성함

'''
첫번째 방법
정답은 나왔으나 시간이 너무 길게 측정됨 + 메모리 사용..
정적배열에서 쓰기 더 좋을듯.
시간 - 348ms
'''

'''
n, k = map(int, input().strip().split(" "))
l = n # 길이 저장용
queue = [i for i in range(1, n + 1)]
check = [False] * n  # 체크 확인용

print("<", end="")
point = -1
while n:
    for i in range (k):
        point = (point+1) % l
        while check[point]:
            point = (point+1) % l
    check[point] = True
    print(queue[point], end="")
    if n == 1:
        print(">", end="")
    else:
        print(", ", end="")
    n -= 1

'''

'''
두번째 방법
이중반복문 대신 pop()을 사용하여 point를 더 빨리 계산하는 방법 생각해보기
시간 - 40ms
'''

n, k = map(int, input().strip().split(" "))
queue = [i for i in range(1, n + 1)]
print("<", end="")
point = 0
while n:  # n == 현재길이
    point = (point + (k - 1)) % n   # 식 도출 가능
    print(queue.pop(point), end="")
    if n == 1:
        print(">", end="")
    else:
        print(", ", end="")
    n -= 1
