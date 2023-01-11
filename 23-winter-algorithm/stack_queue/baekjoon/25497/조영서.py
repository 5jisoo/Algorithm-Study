import sys

n = int(sys.stdin.readline()) #기술 사용 횟수 입력받기
count = 0 #정상적으로 기술을 사용한 횟수
s = []
L,S = 0,0
str = sys.stdin.readline().strip() #\n빼고 문자열 입력받기
for x in str:
    if (x == "L"): #사전 기술 L
        L += 1
    elif (x == "S"): #사전 기술 S
        S += 1
    elif (x == "R"):
        if (L > 0): # 기술 짝이 맞는 경우
            count += 1
            L -= 1
        else:
            break #이후 기술 사용 불가
    elif (x == "K"):
        if (S > 0): #기술 짝이 맞는 경우
            count += 1
            S -= 1
        else:
            break #이후 기술 사용 불가
    else: #연계 없이 사용할 수 있는 기술
        count += 1
print(count)

#n을 사용할 필요가 없다는게 의문