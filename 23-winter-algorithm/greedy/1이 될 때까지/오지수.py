
# 처음 생각한 코드

'''
n, k = map(int, input().split())
count = 0
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
        continue
    else:
        n -= 1
        count += 1

print(count)

'''

n, k = map(int, input().split())
count = 0
while n > 1:
    count += (n % k)  # -1
    n -= (n % k)
    if n == 0:        # n == 0인 경우 count -=1 한 뒤 break
        count -= 1
        break
    n //= k  # k 나누기
    count += 1

print(count)