N = int(input())
for i in range(1,N+1):
    x = input()
    res = ''
    for j in x :
        if j == 'Z':
            res += 'A'
        else :
            res += chr(ord(j)+1)
    print(f'String #{i}')
    print(res)
    print()
