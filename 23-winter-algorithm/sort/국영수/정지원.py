#파이썬의 람다함수에 대해 알면 편함.
#sort함수 이용하면 data.sort(key=lamda x: (-x[1],x[2],-x[3],x[0]))
#sorted함수 이용하면 data = sorted(data, key=lamda x: (-x[1],x[2],-x[3],x[0]))
#오름차순은 양수로, 내림차순은 음수형태로.
N = int(input())
data = []

for _ in range(N):
    a,b,c,d = list(map(str,input().split()))
    data.append( [a, int(b),int(c),int(d)])

data.sort(key = lambda x : (-x[1] , x[2],-x[3],x[0]) )

for i in data :
    print(i[0])