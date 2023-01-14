s = list(input())
t = list(input())

for i in range(len(t) - len(s)):
    if t.pop() == "B":
        t.reverse()

if s == t:
    print("1")
else:
    print("0")