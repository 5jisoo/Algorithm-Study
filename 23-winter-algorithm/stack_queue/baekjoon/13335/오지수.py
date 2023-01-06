'''
트럭 n개가 다리를 건넘
단위 시간당 w씩 트럭들은 이동할 수 있음.
다리의 길이 - w : 다리 위에 w 대의 트럭이 올라갈 수 있음.
다리가 견딜 수 있는 무게 - l

결과 -> 코드는 굉장히 길지만.. 시간은 빨리나옴 :: 코드 줄이는 방법 찾기 필요
'''

n, w, l = map(int, input().split())
weights = list(map(int, input().strip().split()))  # 건너야 할 트럭들의 무게들
bridge = [0] * w  # 다리 위 트럭

count = 0  # 건넌 트럭 개수
clock = 0  # 시간 측정
weight = 0  # 다리의 현재 무게

while count < n:
    if weights and (len(bridge) >= w):  # 현재 다리에 갈 수 있는 칸이 없음
        if bridge[0] > 0:  # 트럭
            count += 1
        weight -= bridge.pop(0)
    if weights:
        if weight + weights[0] <= l:  # 무게 - 진입 가능
            clock += 1
            weight += weights[0]
            bridge.append(weights.pop(0))
        else:  # 무게 - 진입 불가
            clock += 1
            bridge.append(0)
    elif not weights and bridge:
        while bridge:
            clock += 1
            if bridge[0] > 0:
                count += 1
            weight -= bridge.pop(0)

print(clock)
