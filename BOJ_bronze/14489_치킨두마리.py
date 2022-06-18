a,b = map(int,input().split())
c = int(input())

d = c * 2

if a+b >= d :
    print(a+b-d)
else:
    print(a+b)