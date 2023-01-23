'''
322p
문자열 재정렬
'''

string = list(input())
string.sort()

cnt = 0
for s in string:
    if ord("A") <= ord(s) <= ord("Z"):  # 알파벳 - 바로 출력
        print(s, end="")
    else:   # 숫자 - cnt에 더하기
        cnt += int(s)
print(cnt)
