N = int(input())

cnt = 0
for i in range(N+1):
  for j in range(60):
    for k in range(60):
      # 매 시각마다 문자 '3'이 포함되어있으면 개수 증가
      if '3' in str(i) + str(j) + str(k):
        cnt += 1
print(cnt)

# times = [N+1, 60, 60]
# count_three = [0, 0, 0] # 시,분,초 각각의 3 개수세기
# cnt = 0

# for t in range(3): # 시,분,초
#   for i in range(times[t]):
#     share = i // 10
#     left  = i % 10
#     if share == 3 or left == 3:
#       count_three[t] += 1
# print(count_three)
# cnt = count_three[0] * count_three[1] * count_three[2]
# print(cnt)
# 첫 접근의 오류: 위 케이스는 각 시,분,초에 모두 3이 있는 경우의 개수를 구한 것임
# '각 자리에만 3이 있을 때'와 '각 자리와 다른 자리에도 3이 있을 때'를 세면 교집합 케이스가 있으므로 문제 요구상황에서 중복으로 세게 됨 -> 따라서 위 방식으로 접근하면 안됨.

# key: 전체 데이터 개수가 10만개 이하 -> 3중 반복문도 괜찮음, 가능한 경우 모두 검사(브루트포스) ㄱㅊ