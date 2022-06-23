while True:
    n = int(input())
    if n == -1:
        break
    elif n == 6 :
        print('6 = 1 + 2 + 3')
    elif n == 28 :
        print('28 = 1 + 2 + 4 + 7 + 14')
    elif n == 496 :
        print('496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248')
    elif n == 8128:
        print('8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064')
    else :
        print(f'{n} is NOT perfect.')

#-------------------------------------------#

while True:
    n = int(input())
    if n == -1: break
    lst = []
    for i in range(1, n):
        if n%i==0: lst.append(i)
    if sum(lst)==n :
        print(n, " = ", " + ".join(str(j) for j in lst), sep="")
    else : print(f"{n} is NOT perfect.")