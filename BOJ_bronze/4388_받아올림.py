while True:
    x,y = map(int,input().split())
    if x == y == 0:
        break
    else:
        carry = 0
        x, y = str(x), str(y)
        max_len = 0
        if len(x) != len(y):
            max_len = max(len(x),len(y))
        if len(x) == max_len:
            y = '0'* (max_len-len(y)) + y
        else:
            x = '0' * (max_len-len(x)) + x
        cnt = 0
        if max_len == 0 :
            max_len = len(x)
        for i in range(max_len):
            if cnt > 0 :
                sum_xy = int(x[max_len - i - 1]) + int(y[max_len - i - 1]) + cnt
            else :
                sum_xy = int(x[max_len - i - 1]) + int(y[max_len - i - 1])

            if sum_xy >= 10:
                carry += 1
                cnt = 1
            else :
                cnt = 0
        print(carry)

#-----------------------------------------------------------------------------------#
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    k = str(a+b)
    a, b = map(str, [a, b])
    if len(a) < len(b):
        a, b = b, a
    b = '0' * (len(a)-len(b)) + b
    ans = 0
    t = 0
    for i in range(-1, -len(a)-1, -1):
        if int(a[i]) + int(b[i]) + t != int(k[i]):
            ans+=1
            t = 1
        else:
            t = 0
    print(ans)