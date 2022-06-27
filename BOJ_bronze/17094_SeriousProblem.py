n =int(input())
s = input()
e1 = e2 = 0
for i in s:
    if i == '2':
        e1 += 1
    else:
        e2 += 1
if e1 > e2 :
    print(2)
elif e1 < e2 :
    print('e')
else:
    print('yee')