while True:
    x,y,z = input().split()
    y = int(y)
    z = int(z)
    if x == '#':
        break
    if y > 17 or z >= 80:
        print(f'{x} Senior')
    else:
        print(f'{x} Junior')