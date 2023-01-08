from sys import stdin
from collections import deque

def push(x):
    que.append(x)

def pop():
    if len(que)==0:
        return(-1)
    else:
        return que.popleft()
    
def size():
    return len(que)

def empty():
    if len(que) == 0:
        return(1)
    else: 
        return(0)
    
def front():
    if len(que)!= 0:
        return(que[0])
    else:
        return(-1)
    
def back():
    if len(que)!=0:
        return(que[-1])
    else:
        return(-1)
    

N = int(stdin.readline().rstrip())
que = deque()

for i in range(N):
    input = stdin.readline().split()

    order = input[0]

    if order == 'push':
        push(input[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    elif order == 'front':
        print(front())

    elif order == 'back':
        print(back())
