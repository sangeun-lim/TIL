a, b = map(int,input().split())
for i in range(int(input())):
    x = int(input())
    if x <= 1000:
        print(x,x*a)
    else:
        print(x,1000*a + (x-1000)*b)
