#N = input()
#a = list(N)
#i = 0
#if N%2 == 0:
#    for i in range (N/2):
#        i+=1
#여기까지 짜봤는데 if와 for문이 보기 힘들게 겹쳐지고, 리스트에 있는 요소들을 더할 때 리스트 길이 이용하는 방법을 생각못하고 일일히 더해야하나 고민함

n = int(input())
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")