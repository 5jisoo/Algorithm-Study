'''
n = 배열의 크기
m = 숫자가 더해지는 횟수
k = 연속해서 더해질 수 있는 횟수
'''

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()         # 정렬

first = nums[n-1]   # 가장 큰 수
sec = nums[n-2]     # 두번째로 큰 수

add_count = m // (k+1)  # (큰 수 * k번 + 두번째 수 * 1번) 를 반복해서 더할 횟수

total = 0
total += (first*k + sec) * add_count

total += first * (m % (k+1))    # 남은 건 큰수를 더해줌

print(total)