T = int(input())
for tc in range(T):
    n, m = map(int,input().split())
    U = m * 2 - n
    T = m-U
    print(U,T)