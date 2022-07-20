n = int(input())
lst = []
for i in range(n):
    b,p,q,r = map(int,input().split())
    x = p * q * r
    y = p + q + r
    lst.append((b,x,y))
lst2 = sorted(lst, key = lambda x : (x[1], x[2], x[0] ))
for i in lst2[:3]:
    print(i[0], end=' ')