'''
max()는 빈 리스트를 전달하면 에러가 발생하므로,
리스트 원소가 존재할 때만 최대값을 확인하여 더할 수 있도록 함.
'''

n = int(input())
data = list(map(int, input().split()))
d = [1] * n

for i in range(n-1, -1, -1):
    li = [d[j] for j in range(i + 1, n) if data[j] < data[i]]
    if li: 
        d[i] += max(li)

print(n - max(d))