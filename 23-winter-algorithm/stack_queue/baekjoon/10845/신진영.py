from sys import stdin

N = int(stdin.readline())
q_list = []

def queue(q):
  # 큐 구현부
  order = q.split()
  if len(order) == 2:
    q_list.append(order[1])
  else:
    od = order[0]
    if od == "pop":
      tmp = q_list.pop(0) if len(q_list) != 0 else -1
      print(tmp)
    elif od == "size":
      print(len(q_list))
    elif od == "empty":
      tmp = 0 if len(q_list) != 0 else 1
      print(tmp)
    elif od == "front":
      tmp = q_list[0] if len(q_list) != 0 else -1
      print(tmp)
    elif od == "back":
      tmp = q_list[len(q_list)-1] if len(q_list) != 0 else -1
      print(tmp)

for i in range(N):
  in_order = stdin.readline()
  queue(in_order)