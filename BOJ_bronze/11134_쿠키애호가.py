T = int(input())
for tc in range(T):
    n,c = map(int,input().split())
    x = n // c
    if n % c == 0:
        print(x)
    else:
        print(x+1)