def solution(s):
    answer = len(s)
    for length in range(1, len(s) // 2 + 1):  # length
        result = ""
        prev = s[0:length]
        cnt = 1
        for j in range(length, len(s), length):
            if prev == s[j:j + length]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt)
                result += prev
                prev = s[j:j + length]
                cnt = 1
        if cnt > 1:
            result += str(cnt)
        result += prev
        if len(result) < answer:
            answer = len(result)
    return answer


# test
print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
