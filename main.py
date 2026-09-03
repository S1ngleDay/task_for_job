digits = '9876543210'
arr = []

def q(a, i):
    if i == 9:
        arr.append(a)
        return
    i+=1
    q(a+'+'+digits[i], i)
    q(a+'-'+digits[i], i)
    q(a+''+digits[i], i)

q('9', 0)
for i in arr:
    s = 0
    num = ''
    sign = 1
    for j in range(len(i)):
        if i[j].isdigit():
            num += i[j]
        else:
            s += sign*int(num)
            num = ''
            if i[j] == '+':
                sign = 1
            elif i[j] == '-':
                sign = -1
    s += sign*int(num)
    if s==200: print(i)



