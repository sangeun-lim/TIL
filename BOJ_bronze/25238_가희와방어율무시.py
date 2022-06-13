a, b = map(int,input().split())
c = a - a * 0.01 * b

if c < 100 :
    print(1)
else :
    print(0)