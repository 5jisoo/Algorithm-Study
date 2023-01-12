'''
0과 1로 이루어진 문자열 S
숫자가 바뀔때 횟수를 카운트함.

count = 1 일때 답은 1,
count = 2 일때 답은 1, .. 이므로
마지막에 (count + 1) // 2 를 출력해줌.
'''

nums = list(map(int, input()))
prev_num = nums[0]
count = 0
for n in nums:
    if prev_num != n:
        prev_num = n
        count += 1

print((count + 1) // 2)