import sys

n = int(sys.stdin.readline()) #명령의 수 입력받기
l = []
for i in range(n):
    str = sys.stdin.readline().split() #띄어쓰기 단위로 문자열 자르기
    if str[0] == "push":
        l.append(str[1]) #맨뒤에 추가
    elif str[0] == "pop":
        if len(l) != 0:
            print(l.pop(0)) #맨앞 삭제
        else: #리스트에 정수가 없을 경우
            print(-1) 
    elif str[0] == "size":
        print(len(l)) #크기 출력
    elif str[0] == "empty":
        if len(l) == 0: #리스트가 비어있는 경우
            print(1)
        else:
            print(0)
    elif str[0] == "front":
        if len(l) != 0:
            print(l[0]) #맨앞 원소 출력
        else: #리스트에 정수가 없을 경우
            print(-1)
    elif str[0] == "back":
        if len(l) != 0:
            print(l[-1]) #맨뒤 원소 출력
        else: #리스트에 정수가 없을 경우
            print(-1)

