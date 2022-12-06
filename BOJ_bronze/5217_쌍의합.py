N = int(input())
for i in range(N):
    x = int(input())
    s = 1
    e = x-1
    print(f'Pairs for {x}:', end = ' ')
    for j in range((x-1)//2):
        if j != 0 :
            print(',', end= ' ')
        print(s, e, end='')
        s += 1
        e -= 1
    print()

##################################
N = int(input())
for i in range(N):
    x = int(input())
    s = 1
    e = x - 1
    cnt = 0

    print(f'Pairs for {x}: ', end='')
    while s < e:
        if cnt > 0 :
            print(', ', end='')
        if s + e == x :
            print(f'{s} {e}', end='')
            cnt += 1
        s += 1
        e -= 1
    print()