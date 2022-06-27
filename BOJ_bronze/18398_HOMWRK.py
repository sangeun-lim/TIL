T = int(input())
for i in range(T):
    N = int(input())
    for j in range(N):
        A,B = map(int,input().split())
        print(f'{A+B} {A*B}')