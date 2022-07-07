n = int(input())
x1 = y1 = 0
x2 = y2 = 41
for i in range(n):
    x,y = map(int,input().split())
    x1 = max(x,x1)
    y1 = max(y,y1)
    x2 = min(x,x2)
    y2 = min(y,y2)

print( ((x1-x2)+(y1-y2)) * 2)