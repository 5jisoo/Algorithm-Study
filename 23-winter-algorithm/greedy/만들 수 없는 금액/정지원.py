N = int(input())
data = list(map(int, input().split()))
data.sort() #여기까지는 무난히 쓰는데 알고리즘을 어떻게 짤 지 몰라서 헤맸다. 규칙 같은게 있을 줄 알았는데 화폐단위가 작은 순서대로 일일히 확인하고 변수를 바꾸면 됐다. 코드를 보고 이해하는데 초점을 맞췄다.

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)