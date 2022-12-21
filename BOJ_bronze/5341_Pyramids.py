while True:
    n = int(input())
    if n == 0 :
        break
    else :
        cnt = 0
        for i in range(1,n+1):
            cnt += i
        print(cnt)