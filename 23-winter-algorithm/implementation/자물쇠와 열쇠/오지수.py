def rotate(a):  # key 회전 함수
    n = len(a)
    m = len(a[0])
    new_key = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_key[j][n - i - 1] = a[i][j]
    return new_key


def check(new_lock):  # new_lock배열에서 lock이 있는 위치 확인하기
    length = len(new_lock) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for _ in range(4):  # 총 4번 회전
        key = rotate(key)
        for x in range(n * 2):  # key 이동
            for y in range(n * 2):
                for i in range(m):  # key의 원소들을 new_lock에 더해주기
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):  # new_lock의 lock부분 원소 체크
                    return True
                for i in range(m):  # 더했던 key를 다시 빼줌
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


# test
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
