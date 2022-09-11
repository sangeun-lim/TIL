n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    if (x <= 1 and y <= 2) or (x <=2 and y <=1 ):
        print('Yes')
    else:
        print('No')