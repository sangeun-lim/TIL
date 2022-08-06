def gcd(x,y):
    while y > 0 :
        x,y = y, x %y
    return x

T = int(input())
for tc in range(T):
    a,b = map(int,input().split())
    print(gcd(a,b) * a//gcd(a,b) * b//gcd(a,b), gcd(a,b))