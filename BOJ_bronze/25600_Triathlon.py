N = int(input())
res = 0
for i in range(N):
    a,d,g = map(int,input().split())
    if a == (d+g) :
        x = 2 * a * (d+g)
    else :
        x = a * (d + g)
    res = max(res,x)
print(res)
