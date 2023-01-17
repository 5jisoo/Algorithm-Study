'''
321p 럭키 스트레이트
'''
scores = list(map(int, input()))
left = 0

n = len(scores) // 2

if sum(scores[:n]) == sum(scores[n:]):
    print("LUCKY")
else:
    print("READY")
