'''
- input
n = 동전의 개수
동전의 종류
'''

n = int(input())
coins = list(map(int, input()))
coins.sort()

result = 1

for c in coins:
    if result < c:
        break
    result += c

print(result)
