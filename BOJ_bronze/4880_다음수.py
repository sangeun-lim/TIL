while True:
    x,y,z = map(int,input().split())
    if x == y == z == 0:
        break
    else :
        if y-x == z-y:
            print(f'AP {z+(z-y)}')
        else:
            print(f'GP {z * (z//y)}')