n, m = map(int, input().split())
book_list = list(map(int, input().split()))

book_plus = [x for x in book_list if x > 0]
book_plus.sort(reverse=True)  # 내림차순 정렬 - 가장 먼 곳부터 책을 두기 위해

book_minus = [abs(x) for x in book_list if x < 0]  # 절댓값으로 저장
book_minus.sort(reverse=True)

max_distance = 0
if book_minus:
    max_distance = max(max_distance, book_minus[0])
if book_plus:
    max_distance = max(max_distance, book_plus[0])

result = 0

for j in range(0, len(book_plus), m):
    if book_plus[j] == max_distance:
        continue
    result += book_plus[j]

for k in range(0, len(book_minus), m):
    if book_minus[k] == max_distance:
        continue
    result += book_minus[k]

result *= 2
result += max_distance

print(result)
