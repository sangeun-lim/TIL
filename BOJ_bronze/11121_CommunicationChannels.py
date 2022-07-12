T = int(input())
for i in range(T):
    x,y = map(str,input().split())
    if x == y :
        print('OK')
    else:
        print('ERROR')