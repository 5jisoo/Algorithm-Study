n = int(input())
count = 0

st_LR = []  # stack
st_SK = []
skills = list(input().strip())
for skill in skills:
    if ord("1") <= ord(skill) <= ord("9"):
        # print("1~9")  # test
        count += 1
    elif skill == "S":
        st_SK.append(skill)
    elif skill == "L":
        st_LR.append(skill)
    elif skill == "R":
        if st_LR:
            st_LR.pop()
            count += 1
        else:
            break
    elif skill == "K":
        if st_SK:
            st_SK.pop()
            count += 1
        else:
            break

print(count)
