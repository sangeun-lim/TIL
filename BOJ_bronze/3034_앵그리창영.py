n,w,h = map(int,input().split())
for i in range(n):
    a = int(input())
    x = (w ** 2 + h ** 2) ** 0.5
    if a <= x :
        print('DA')
    else:
        print('NE')