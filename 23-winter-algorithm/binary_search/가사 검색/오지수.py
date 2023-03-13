'''
# try 1
# 정확도 테스트 통과, 효율성 테스트 탈락한 코드

def binary_search(word, query, start, end):
    n = len(query)
    if start > end:
        return 1
    mid_idx = (start + end) // 2

    answer = 1
    if query[mid_idx] == "?":
        if query[n - 1] == "?":  # ?? 가 접미사인 경우
            answer *= binary_search(word, query, start, mid_idx - 1)  # 앞에서 탐색
        else:  # 접두사인 경우
            answer *= binary_search(word, query, mid_idx + 1, end)  # 뒤에서 탐색
    elif query[mid_idx] != word[mid_idx]:  # word가 query에 맞지 않는 경우
        return 0
    else:
        answer *= binary_search(word, query, start, mid_idx - 1)
        answer *= binary_search(word, query, mid_idx + 1, end)
    return answer


def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        n = len(query)
        for word in words:
            if n != len(word):
                continue
            start = 0
            end = n - 1
            if binary_search(word, query, start, end):
                cnt += 1
        answer.append(cnt)
    return answer

'''


'''
# try 2
# 어림도 없음

def find_section(query):
    # ??를 제외한 단어가 어디서부터 시작, 끝나는지?
    n = len(query)

    # result
    start_idx = 0
    end_idx = n - 1

    # find
    start = 0
    end = n - 1

    if query[n - 1] == "?":  # 접미사
        while start <= end:
            mid = (start + end) // 2
            if query[mid] == "?":
                start_idx = mid
                end = mid - 1
            else:
                start = mid + 1
        end_idx = start_idx - 1
        start_idx = 0

    else:  # 접두사
        while start <= end:
            mid = (start + end) // 2
            if query[mid] == "?":
                end_idx = mid
                start = mid + 1
            else:
                end = mid - 1
        start_idx = end_idx + 1
        end_idx = n - 1

    return start_idx, end_idx


def binary_search(word, query, start, end):
    if start > end:
        return 1
    mid_idx = (start + end) // 2

    answer = 1
    if query[mid_idx] != word[mid_idx]:  # word가 query에 맞지 않는 경우
        return 0
    else:
        answer *= binary_search(word, query, start, mid_idx - 1)
        answer *= binary_search(word, query, mid_idx + 1, end)
    return answer


def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        word_start, word_end = find_section(query)
        for word in words:
            if len(query) != len(word):
                continue
            if binary_search(word, query, word_start, word_end):
                cnt += 1
        answer.append(cnt)
    return answer

'''

# try 3

from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx


array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != "?":
            cnt = count_by_range(array[len(query)], query.replace('?', 'a'),
                                 query.replace('?', 'z'))
        else:
            cnt = count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'),
                                 query[::-1].replace('?', 'z'))
        answer.append(cnt)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?"]))
