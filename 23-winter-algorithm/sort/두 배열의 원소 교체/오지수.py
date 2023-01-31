n, k = map(int, input().split())
data_a = list(map(int, input().split()))
data_b = list(map(int, input().split()))

data_a.sort()
data_b.sort(reverse=True)

for i in range(k):
    if data_a[i] < data_b[i]:
        data_a[i], data_b[i] = data_b[i], data_a[i]
    else:
        break

print(sum(data_a))
