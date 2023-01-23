k = int(input())
data = []
width = 0
height = 0

lengths = []
max_height = 0
max_width = 0
h_idx = 0
w_idx = 0

for i in range(6):
    dic, length = map(int, input().split())
    lengths.append(length)
    if (dic == 1 or dic == 2) and length >= max_height:
        max_height = length
        h_idx = i
    elif (dic == 3 or dic == 4) and length >= max_width:
        max_width = length
        w_idx = i

subH = abs(lengths[(h_idx - 1) % 6] - lengths[(h_idx + 1) % 6])
subW = abs(lengths[(w_idx - 1) % 6] - lengths[(w_idx + 1) % 6])
area = (max_height * max_width - subH * subW) * k
print(area)


'''
# 이거 처음에 제출한 코드인데 반례 부탁드림다..

k = int(input())
data = []
width = 0
height = 0

lengths = []
max_height = 0
max_width = 0
fir_idx = 0
sec_idx = 0

for i in range(6):
    dic, length = map(int, input().split())
    lengths.append(length)
    if (dic == 1 or dic == 2) and length >= max_height:
        max_height = length
        fir_idx = i
    elif (dic == 3 or dic == 4) and length >= max_width:
        max_width = length
        sec_idx = i

if fir_idx > sec_idx:
    fir_idx, sec_idx = sec_idx, fir_idx

area = max_height * max_width - lengths[(fir_idx - 2) % 6] * lengths[(sec_idx + 2) % 6]
print(area * k)



'''