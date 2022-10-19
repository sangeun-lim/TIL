g, p , t = map(int,input().split())
x = g * p
y = g + p * t
if x > y :
    print(2)
elif x < y :
    print(1)
else:
    print(0)