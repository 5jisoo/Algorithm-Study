n = int(input())
data = []

for _ in range(n):
    name, language, english, math = input().split()
    data.append((name, int(language), int(english), int(math),))

data.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for name, language, english, math in data:
    print(name)

