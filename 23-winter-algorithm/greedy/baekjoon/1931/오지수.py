import sys
input = sys.stdin.readline  # 이 문제는 특이하게 이걸 사용해야 시간이 굉장히 빨라짐....

n = int(input())  # 회의 수

times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append((start, end))

times = sorted(times, key=lambda x: (x[1], x[0]))

end = 0  # 이전 회의가 끝난시간
count = 0

for (s, e) in times:
    if s >= end:
        end = e
        count += 1

print(count)