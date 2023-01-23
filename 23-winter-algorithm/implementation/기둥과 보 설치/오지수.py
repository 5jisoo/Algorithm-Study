def possible(building):  # 현재 구조물이 가능한 구조물인지 확인
    for x, y, a in building:
        if a == 0:  # 기둥인 경우
            if y == 0 or [x - 1, y, 1] in building or [x, y, 1] in building or [x, y - 1, 0] in building:   # 여기서 조건 하나를 빼먹었음.. 유의해서 풀기
                continue
            return False
        elif a == 1:  # 보인 경우
            if [x, y - 1, 0] in building or [x + 1, y - 1, 0] in building or (
                    [x + 1, y, 1] in building and [x - 1, y, 1] in building):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            answer.append([x, y, a])
            if not possible(answer):  # 불가능한 경우
                answer.remove([x, y, a])
        elif b == 0:  # 삭제
            answer.remove([x, y, a])
            if not possible(answer):  # 불가능한 경우
                answer.append([x, y, a])
    return sorted(answer)


print(solution(5,
               [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1],
                [4, 2, 1, 1],
                [3, 2, 1, 1]]))

print(solution(5,
               [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
                [3, 1, 1, 1],
                [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
