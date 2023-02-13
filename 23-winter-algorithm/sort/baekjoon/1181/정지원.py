#리스트이름.sort(key=len)->sort는 문자열을 정렬하는 기능도 있음. 저 코드로 문자열 길이 순으로 정렬 가능.
#같은 단어는 한번만 출력된다는 조건 때문에 중복 제거도 고려.
n = int(input())

a = []
for _ in range(n):
    a.append(input())

set = set(a) #Q.이게 어떻게 중복 제거가 되는지 모르겠음..if문 이용해서 중복제거하는 다른 방법은 없으려나?
list = list(set)

list.sort()
list.sort(key=len)

for i in list:
    print(i)