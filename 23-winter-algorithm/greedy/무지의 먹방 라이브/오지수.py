import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
        
    q = []  # min heap
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 min heap에 저장
        heapq.heappush(q, (food_times[i], i + 1))

    n = len(food_times)  # 음식 개수
    sum_value = 0  # 먹기 위해 사용한 시간
    prev = 0  # 직전에 다 먹은 음식의 시간

    # 시간 충분한 경우
    while sum_value + ((q[0][0] - prev) * n) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * n
        n -= 1
        prev = now

    # 시간이 충분하지 않은 경우
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % n][1]