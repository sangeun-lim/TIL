T = int(input())
for i in range(T):
    lst = list(map(int,input().split()))
    print(*lst)
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for j in lst:
        if j == 17 :
            cnt1 += 1
            cnt3 += 1
        if j == 18 :
            cnt2 += 1
            cnt3 += 1
    if cnt3 == 2 :
        print('both')
    else :
        if cnt1 == 1 :
            print('zack')
        elif cnt2 == 1 :
            print('mack')
        else:
            print('none')
    print()

########################
n=int(input())
for _ in range(n):
    l=list(map(int, input().split()))
    print(*l)
    if 17 in l and 18 in l: print('both')
    elif 17 in l: print('zack')
    elif 18 in l: print('mack')
    else: print('none')
    print()