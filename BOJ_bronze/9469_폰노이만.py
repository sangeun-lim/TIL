P = int(input())
for i in range(P):
    N,D,A,B,F = map(float,input().split())
    N = int(N)
    x = D/(A+B)
    print(f'{N} {F*x:.6f}')