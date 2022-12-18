T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    if a == 1 :
        print(a,b)
        print(b)
    else:
        print(a,b)
        print(a*b - (a-1)*2)