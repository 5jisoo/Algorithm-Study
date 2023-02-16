import sys

n = int(sys.stdin.readline())
l = [0] * 1000001

for i in range(2,n+1):
    l[i] = l[i-1] + 1 #1을 빼는 경우
    if (i % 3 == 0): #3으로 나누는 경우
        l[i] = min(l[i], l[i//3] + 1)
    if (i % 2 == 0): #2로 나누는 경우
        l[i] = min(l[i], l[i//2] + 1)
    
print(l[n])
