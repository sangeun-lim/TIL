lst = list(map(int,input().split()))
lst.sort()
x = min(lst[2] - lst[1] , lst[1]-lst[0])
if lst[0] + x in lst:
    if lst[0] + x + x in lst:
        print(lst[0]+x+x+x)
    else:
        print(lst[0]+x+x)
else :
    print(lst[0]+x)