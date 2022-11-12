T = int(input())
for i in range(T):
    a,b,c,d = map(int,input().split())
    x = a * b
    y = c * d
    if x > y :
        print('TelecomParisTech')
    elif x < y :
        print('Eurecom')
    else :
        print('Tie')