# 백준 10799번
# 쇠막대기

brackets = list(input().strip())
st = []     # stack - "(" 저장. : 막대기 저장
flag = 1    # 1이면 레이저
count = 0
for bracket in brackets:
    if bracket == "(":
        st.append(bracket)
        flag = 1
    else:  # ")" 인 경우
        if flag:                          # 레이저인 경우
            st.pop()
            count += len(st)              # 현재 막대기 개수 더하기
        else:                             # 막대기의 끝인 경우 - 마지막조각 1 더해주고 끝
            p = st.pop()                  
            count += 1
        flag = 0
print(count)