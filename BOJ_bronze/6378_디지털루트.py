while True:
    x = input()
    if x == '0':
        break
    else :
        cnt = 0
        for i in x:
            cnt += int(i)
        if cnt < 10 :
            print(cnt)
        else :
            cnt2 = 0
            for j in str(cnt):
                cnt2 += int(j)
            if cnt2 < 10 :
                print(cnt2)
            else :
                cnt3 = 0
                for k in str(cnt2):
                    cnt3 += int(k)
                print(cnt3)

############################################
while True:
    num = input()
    if num =='0':
        break
    while len(num) != 1:
        a = 0
        for i in num:
            a += int(i)
        num = str(a)
    print(num)