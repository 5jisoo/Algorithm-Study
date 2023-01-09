# 백준 5397번
# 키로거

test = int(input())
for t in range(test):
    st_left = []    # insert나 pop(0) 등은 성능이 떨어지므로 left와 right stack을 각각 만들어 주어야 함.
    st_right = []
    string = list(input().strip())
    for s in string:
        if s == "<":
            if st_left:
                st_right.append(st_left.pop())
        elif s == ">":
            if st_right:
                st_left.append(st_right.pop())
        elif s == "-":
            if st_left:
                st_left.pop()
        else:
            st_left.append(s)
    st_left.extend(reversed(st_right))
    print("".join(st_left))