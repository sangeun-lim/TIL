a,b,c = map(int,input().split())
t1 = a*24*60 + b*60 + c
t2 = 11*24*60 + 11 * 60 + 11
t = t1-t2

if t < 0 :
    print(-1)
else:
    print(t)