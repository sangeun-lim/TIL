x = input()
res = ''
for i in x:
    if i == 'I':
        res += 'E'
    elif i == 'E':
        res += 'I'
    elif i == 'S':
        res += 'N'
    elif i == 'N':
        res += 'S'
    elif i == 'T':
        res += 'F'
    elif i == 'F':
        res += 'T'
    elif i == 'P':
        res += 'J'
    else:
        res += 'P'
print(res)

######################################
x = input()
res = ['I','E','S','N','T','F','P','J']
for i in x:
    res.remove(i)
print(''.join(res))