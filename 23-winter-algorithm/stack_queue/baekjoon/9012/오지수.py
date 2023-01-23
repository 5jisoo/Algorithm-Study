# replace() 함수 사용 제외 시간도 빠름

t = int(input())
count = 0

while t > 0:
    st = []     # stack
    words = list(input().strip())
    if len(words) % 2 == 1:
        print("NO")
        t -= 1
        continue
    for word in words:
        if not st:
            st.append(word)
        else:
            if word == ")" and st[-1] == "(":
                st.pop()
            else:
                st.append(word)
    if not st:
        print("YES")
    else:
        print("NO")
    t -= 1