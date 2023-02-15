cnt = 1
while True:
    a, b, c = map(int,input().split())
    if a == b == c == 0:
        break
    else:
        if a == -1:
            a = (c ** 2 - b ** 2) ** 0.5
            if type(a) == type(1j) or a == 0:
                print(f'Triangle #{cnt}')
                print('Impossible.')
            else:
                print(f'Triangle #{cnt}')
                print(f'a = {a:.3f}')
        elif b == -1:
            b = (c ** 2 - a ** 2) ** 0.5
            if type(b) == type(1j) or b == 0:
                print(f'Triangle #{cnt}')
                print('Impossible.')
            else:
                print(f'Triangle #{cnt}')
                print(f'b = {b:.3f}')
        else:
            c = (a ** 2 + b ** 2) ** 0.5
            if type(c) == type(1j) or c == 0:
                print(f'Triangle #{cnt}')
                print('Impossible.')
            else:
                print(f'Triangle #{cnt}')
                print(f'c = {c:.3f}')
    print()
    cnt += 1
#------------------------------------------------------------#
cnt = 1
while True:
    a, b, c = map(int,input().split())
    if a == b == c == 0:
        break
    else:
        if cnt > 1:
            print()
        print(f'Triangle #{cnt}')
        if c == -1:
            print(f'c = {(a ** 2 + b ** 2) ** 0.5:.3f}')
        elif max(a,b) >= c:
            print('Impossible.')
        elif a == -1:
            print(f'a = {(c ** 2 - b ** 2) ** 0.5:.3f}')
        elif b == -1:
            print(f'b = {(c ** 2 - a ** 2) ** 0.5:.3f}')
        cnt += 1