n = int(input())
dot_list = [tuple(map(int, input().split())) for _ in range(n)]
dot_list.sort()

result = 0
line_start = dot_list[0][0]
line_end = dot_list[0][1]
for start, end in dot_list:
    if start <= line_end:
        if end >= line_end:
            line_end = end  # start 기준으로 sort했으므로 line_start를 update하는 경우는 없음.
    else:
        result += (line_end - line_start)
        line_start = start
        line_end = end

result += (line_end - line_start)  # 마지막 선 더하기
print(result)
