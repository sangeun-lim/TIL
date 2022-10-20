a, b = map(int,input().split())
c, d = map(int,input().split())

x1 = a/c + b/d
x2 = c/d + a/b
x3 = d/b + c/a
x4 = b/a + d/c

res = max(x1,x2,x3,x4)
if res == x1 :
    print(0)
elif res == x2:
    print(1)
elif res == x3:
    print(2)
else:
    print(3)
###############################