for i in range(int(input())):
    total = 0
    for j in range(int(input())):
        a,b,c = map(int,input().split())
        if max(a,b,c) > 0 :
            total += max(a,b,c)
        else :
            total += 0
    print(total)