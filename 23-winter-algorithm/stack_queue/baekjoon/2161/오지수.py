n = int(input())
queue = []

for num in range(1, n+1):
    queue.append(num)       # 큐에 숫자 넣기

# 이 표현이 더 좋아보임 => 하지만 당연히 시간은 동일함
# queue = [ i for i in range(1, n+1)]

while len(queue) != 1:
    print(queue.pop(0))     # 제일 위에 있는 카드 버리기
    first = queue.pop(0)    # 제일 위에 있는 카드 맨 아래로 이동
    queue.append(first)

print(queue.pop(0))         # 마지막 숫자 출력
