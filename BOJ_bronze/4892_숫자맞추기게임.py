x = 1
while True:
    n0 = int(input())
    if n0 == 0 :
        break
    n1 = n0*3
    if n1 % 2 == 0 :
        n2 = n1//2
    else :
        n2 = (n1+1)//2

    n3 = n2*3
    n4 = n3 // 9
    if n0 % 2 == 0 :
        print(f'{x}. even {n4}')
    else:
        print(f'{x}. odd {n4}')
    x += 1