import sys
input = sys.stdin.readline      # 빠를 수도 있고 안빠를 수도 있음^^..?

n = int(input())
count = 0

while n:
    st = []     # stack
    string = list(input().strip())      # strip(): 마지막 줄 바꿈 문자 제거
    if len(string) % 2 == 1:  # 길이가 홀수면 그냥 넘기기
        n-=1
        continue
    for i in string:
        if not st:              # stack에 아무것도 없다면 그냥 넣기
            st.append(i)
        else:
            if st[-1] == i:     # stack의 마지막 단어와 동일하다면 stack.pop()
                st.pop()
            else:
                st.append(i)    # 동일하지 않으면 그냥 넣기
    if not st:                # string의 단어들을 모두 pop하고 난 뒤, stack의 길이가 0이면 좋은 단어
        count += 1
    n -= 1

print(count)