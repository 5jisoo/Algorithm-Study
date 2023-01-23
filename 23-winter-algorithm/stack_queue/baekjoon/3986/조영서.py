import sys

n = int(sys.stdin.readline()) #단어의 수 입력받기
count = 0 #좋은 단어의 수
for i in range(n):
    str = sys.stdin.readline().strip() #\n빼고 문자열 입력받기
    s = [] #리스트 초기화
    for x in str:
        if (len(s) == 0): 
            s.append(x) #무조건 원소 추가
        else:
            if (x == s[-1]): #짝 지어지는 경우
                s.pop() #원소 제거
            else: #짝 지어지지 않는 경우
                s.append(x) #원소 추가
    if (len(s) == 0): #좋은 단어인 경우
        count += 1
print(count)


