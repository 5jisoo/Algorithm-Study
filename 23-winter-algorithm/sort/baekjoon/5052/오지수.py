test_case = int(input())

for _ in range(test_case):
    n = int(input())
    number_list = [input() for _ in range(n)]  # 숫자가 아닌 문자열로 입력받음
    number_list.sort()  # 문자열 sort 규칙 참고

    prefix = number_list[0]
    flag = 1  # flag 변수
    for number in number_list[1:]:
        if number.find(prefix) == 0:
            flag = 0
            print("NO")
            break
        prefix = number
    if flag:
        print("YES")
