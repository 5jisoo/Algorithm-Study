n = int(input())
words = []

for _ in range(n):
    words.append(input())

words = list(set(words))
words.sort()
words.sort(key=len) # 길이 순으로 정렬하기

for word in words:
    print(word)