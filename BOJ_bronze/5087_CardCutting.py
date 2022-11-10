while True:
    lst = list(map(str,input().split()))
    if '#' in lst:
        break
    else :
        cnt1 = 0
        cnt2 = -1
        for i in lst :
            if i in 'A3579':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 > cnt2:
            print('Cheryl')
        elif cnt1 < cnt2:
            print('Tania')
        else:
            print('Draw')