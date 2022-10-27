while True:
    a, b = map(int,input().split())
    if a == b == 0 :
        break
    else:
        x = min(a,b)
        y = max(a,b)
        z = 3 * x
        print(z-x-y)