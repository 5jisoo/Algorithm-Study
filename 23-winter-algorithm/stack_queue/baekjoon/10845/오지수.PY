import sys
input = sys.stdin.readline      # 이걸로 시간 초과 해결 가능

class QUEUE:
    que = []

    def __int__(self):
        self.que = []

    def main(self, command):  # command는 리스트
        if command[0] == "push":
            self.push(command[1])
        elif command[0] == "pop":
            self.pop()
        elif command[0] == "front":
            self.front()
        elif command[0] == "back":
            self.back()
        elif command[0] == "empty":
            self.empty()
        elif command[0] == "size":
            self.size()

    def push(self, num):
        self.que.append(num)

    def pop(self):
        if self.is_empty():
            print("-1")
        else:
            print(self.que.pop(0))

    def front(self):
        if self.is_empty():
            print("-1")
        else:
            print(self.que[0])

    def back(self):
        if self.is_empty():
            print("-1")
        else:
            print(self.que[-1])

    def empty(self):
        if self.que:
            print("0")
        else:
            print("1")

    def is_empty(self):  # return 용
        if self.que:
            return 0
        else:
            return 1

    def size(self):
        print(len(self.que))


n = int(input())
q = QUEUE()
while n:
    command = input().strip().split(" ")
    # print(command)  # test
    q.main(command)
    n -= 1
