from itertools import permutations
from collections import deque


n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

operator = ["add"] * add + ["sub"] * sub + ["mul"] * mul + ["div"] * div

min_result = 1e9
max_result = -1e9
order = list(permutations(operator, len(operator)))
for operators in order:
    number = deque(nums)
    first = number.popleft()
    for op in operators:
        sec = number.popleft()
        if op == "add":
            first += sec
        elif op == "sub":
            first -= sec
        elif op == "mul":
            first *= sec
        elif op == "div":
            if first < 0:
                first *= -1
                first //= sec
                first *= -1
            else:
                first //= sec
    min_result = min(min_result, first)
    max_result = max(max_result, first)
print(max_result)
print(min_result)
