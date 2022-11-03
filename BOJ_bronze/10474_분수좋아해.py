while True:
    x,y = map(int,input().split())
    if x == y == 0 :
        break
    else:
        z = x // y
        zz = x % y
        print(f'{z} {zz} / {y}')