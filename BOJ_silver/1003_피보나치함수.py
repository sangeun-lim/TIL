# 시간초과 뜸
def dp(n):
    global cnt0, cnt1
    if n == 0 :
        cnt0 += 1
        return 0
    elif n == 1 :
        cnt1 += 1
        return 1
    else :
        return dp(n-1) + dp(n-2)

T = int(input())
for tc in range(T):
    n = int(input())
    cnt0 = cnt1 = 0
    dp(n)

    print(f'{cnt0} {cnt1}')

######################################

T = int(input())
for tc in range(T):
    n = int(input())
    cnt0 = [1,0]
    cnt1 = [0,1]
    if n >= 2 :
         for i in range(n-1):
             cnt0.append(cnt1[-1])
             cnt1.append(cnt0[-2]+cnt1[-1])
    print(cnt0[n],cnt1[n])
