n = int(input())
for i in range(n):
    n,m = map(int,input().split())
    res = 0
    for j in range(n,m+1):
        x = str(j)
        res += x.count('0')
    print(res)