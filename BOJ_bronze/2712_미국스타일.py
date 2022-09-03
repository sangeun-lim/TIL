T = int(input())
for i in range(T):
    x, y = input().split()
    x = float(x)
    if y == 'kg':
        print(f'{x*2.2046:.4f} lb')
    elif y == 'l':
        print(f'{x*0.2642:.4f} g')
    elif y == 'lb':
        print(f'{x*0.4536:.4f} kg')
    else :
        print(f'{x*3.7854:.4f} l')