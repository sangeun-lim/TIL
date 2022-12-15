T = int(input())
for i in range(T):
    a,b,c = map(int,input().split())
    x = a
    y = b
    for j in range(c):
        if x >= y :
            z = x // 2
            x = z
        else :
            z = y // 2
            y = z
    print(f'Data set: {a} {b} {c}')
    print(max(x,y),min(x,y))
    print()
