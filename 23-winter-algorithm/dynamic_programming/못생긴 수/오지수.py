'''
n = int(input())
d = [1] * n
for i in range(1, n):
    min_value = 1e10
    for j in range(i):
        for t in [2, 3, 5]:
            if d[j] * t > d[i-1] and d[j] * t < min_value:
                d[i] = d[j] * t
                min_value = d[j]*t

print(d[n-1])
'''

'''
반복문.. 다시 풀었음
'''
n = int(input())
d = [0] * n
d[0] = 1 

i2= i3= i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    d[i] = min(next2, next3, next5)
    if d[i] == next2:
        i2 += 1
        next2 = d[i2] * 2
    if d[i] == next3:
        i3 += 1
        next3 = d[i3] * 3
    if d[i] == next5:
        i5 += 1
        next5 = d[i5] * 2

print(d[n-1])