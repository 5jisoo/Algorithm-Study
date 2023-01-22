# 알파벳이랑 숫자 어떻게 구분할지 모르겠어서 헤매고 검색해봤음. 
#파이썬 숫자 확인=isdemical, 알파벳 확인=isalpha인 것 기억해두기!
#리스트의 오름차순은 sorted 함수 이용하면 됨. Q.sort랑 sorted함수의 차이가 뭐지? -> 'sorted(리스트이름)', '리스트이름.sort()=정렬, 리스트이름=출력'의 구조임
#Q.리스트를 문자열로 변환하는건 어떻게하지? -> ' '.join(리스트이름) 이렇게 하면 띄어쓰기 없는 하나의 문장으로 변환됨. print(' '.join(리스트이름)) 하면 변환된 문장 출력.
string = input()
list = []
result = 0
for i in string:
    if i.isalpha():
        list.append(i)
    else:
        result += int(i) #int형으로 바꿔줘야 계산가능해짐
list.sort()
print(''.join(list)+str(result)) #''.join을 하면 띄어쓰기 없이 출력되고 ' '.join으로 하면 띄어쓰기 있게 출력됨

