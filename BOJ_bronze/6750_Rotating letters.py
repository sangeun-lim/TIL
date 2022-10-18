x = input()
y = len(x)
cnt = 0
for i in x :
    if i in 'IOSHZXN':
        cnt += 1
if cnt == y:
    print('YES')
else:
    print('NO') 