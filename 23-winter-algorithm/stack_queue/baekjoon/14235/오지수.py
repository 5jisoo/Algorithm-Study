import sys
input = sys.stdin.readline

st = []

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if st:
            print(st.pop())
        else:
            print("-1")
    else:
        for gift in a[1:]:
            st.append(gift)
        st.sort()

'''
시간이 너무 느림 ==> 시간이 빠른 경우는 heapq 라이브러리 사용하는 예시들밖에 없는듯.
라이브러리 사용하지 않고, 더 빠른 방법이 있을까에 대해 생각해봐야 할듯. (삽입정렬 시도해봤으나 더 오래걸림)
'''