#여기는 코드 어떻게 짜야할 지 감이 안잡혀서 코드 보면서 공부하는 형식으로 함

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 +=1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
            
print(min(count0, count1))