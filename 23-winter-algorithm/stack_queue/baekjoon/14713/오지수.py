# 백준 14713
# 앵무새

n = int(input())
data = []
count = 0

for i in range(n):
    new_data = list(input().split())
    data.append(new_data)
    count += len(new_data)

sentence = list(input().split())

if count != len(sentence):
    print("Impossible")
    exit(0)

possible = 1
for word in sentence:
    check = 0
    for d in data:
        if d and word == d[0]:
            d.pop(0)
            check = 1
    if check == 0:
        possible = 0
        break

if possible:
    print("Possible")
else:
    print("Impossible")
