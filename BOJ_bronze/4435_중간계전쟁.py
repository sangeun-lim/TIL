N = int(input())
for i in range(1,N+1):
    a,b,c,d,e,f = map(int,input().split())
    aa,bb,cc,dd,ee,ff,gg = map(int,input().split())
    x = a + 2*b + 3*c + 3*d + 4*e + 10*f
    y = aa + 2*(bb+cc+dd) + 3*ee + 5*ff + 10*gg
    if x < y :
        print(f'Battle {i}: Evil eradicates all trace of Good')
    elif x > y :
        print(f'Battle {i}: Good triumphs over Evil')
    else :
        print(f'Battle {i}: No victor on this battle field')