num = input()

result = int(num[0])
for i in range(0, len(num)):
    if int(num[i]) <= 1: #여기서 0인 경우에만 더해주면 된다고 생각하고 1을 고려못함..경우 빼놓지 않게 주의해야겠음
        result += int(data[i])
    else:
        result *= num
print(result)
