while True:
    x, y, z = input().split()
    if x == '0' and y == 'W' and z == '0':
        break
    else:
        if y == 'W':
            res = int(x) - int(z)
            if res >= -200:
                print(res)
            else:
                print('Not allowed')
        else :
            res = int(x) + int(z)
            print(res)