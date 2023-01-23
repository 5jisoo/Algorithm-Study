N = int(input())
groupword = 0
for i in range(N):
    string = input()
    error = 0
    for index in range(len(string)-1):
        if word[index] != word[index+1]:
            string2 = string[index+1:]
            if string2.count(word[index])>0:
                error += 1
    if error == 0:
        groupword += 1
print(groupword)




