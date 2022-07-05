T = int(input())
for tc in range(T):
    n = int(input())
    total = 0
    T = 0
    for i in range(1,n+1):
        for j in range(1, i+2):
            T += j
        total += i * T
        T = 0
    print(total)

################################################
T = int(input())
for tc in range(T):
    n = int(input())
    a=0
    for i in range(1,n+1):
        a += (i+1)*(i+2)*i//2
    print(a)