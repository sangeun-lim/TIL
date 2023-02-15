while True:
    B,N = map(int,input().split())
    if B == N == 0:
        break
    else:
        cnt = 1
        lst = []
        while True :
            x = cnt
            cnt = cnt ** N
            lst.append((abs(cnt-B),x))
            if cnt > B:
                break
            cnt = x + 1
        lst.sort()
        print(lst[0][1])

#-------------------------------------------#

B, N = map(int, input().split())

while B:
    if N == 1: print(B)
    else:
        k = 1
        while pow(k, N) < B:
            k += 1
        print([k, k - 1][abs(pow(k - 1, N) - B) < abs(pow(k, N) - B)]) # 처음보는 문법
    B, N = map(int, input().split())