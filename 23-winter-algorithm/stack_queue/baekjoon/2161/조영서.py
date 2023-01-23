import sys

n = int(sys.stdin.readline()) #카드 수 입력받기
card = [ i for i in range(1, n+1)] #카드 생성
while len(card) != 1: 
    print(card.pop(0), end=' ') #버리는 카드 출력
    card.append(card.pop(0)) #카드 옮기기
print(card[0]) #마지막 카드 출력

