import sys
input = sys.stdin.readline

n = int(input())
st = []  # stack
count = 0  # count 사용한다는 점
result = [] # 리스트 사용이 문자열 연산보다 훨씬빠름
flag = 1  # 1이면 배열 생성가능

for i in range(n):
    num = int(input())
    while count < num:
        count += 1
        st.append(count)
        result.append("+")
    if st[-1] == num:
        st.pop()
        result.append("-")
    else:
        print("NO")
        flag = 0
        break

if flag:
    for i in result:
        print(i)