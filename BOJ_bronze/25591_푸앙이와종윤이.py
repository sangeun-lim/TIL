x,y = map(int,input().split())
a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
if d > 99:
    q = d // 100
    r = d % 100
else :
    q = 0
    r = d

print(a,b,c,d,q,r)
print(c+q, r)