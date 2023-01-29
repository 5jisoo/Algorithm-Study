from collections import deque


def check(str_list):
    data = deque(str_list)
    stack = []
    while data:
        d = data.popleft()
        if stack and stack[-1] == "(" and d == ")":
            stack.pop()
        else:
            stack.append(d)
    if not stack:
        return True
    else:
        return False


def solution(p):
    answer = ""
    string = deque(p)
    if not string:
        return answer
    u = []
    v = []

    cnt = 0
    while True:  # u와 v 나눔
        data = string.popleft()
        u.append(data)
        if data == "(":
            cnt += 1
        else:
            cnt -= 1
        if not cnt:
            break
    while string:
        v.append(string.popleft())

    if check(u):
        answer += "".join(u)
        answer += solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer


# test
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
