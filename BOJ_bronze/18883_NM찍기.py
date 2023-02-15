N,M = map(int,input().split())
x = 1
for i in range(N):
    for j in range(M):
        if j != M-1 :
            print(x, end=' ')
        else:
            print(x, end='')
        x += 1
    print()