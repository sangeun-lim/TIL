import sys
sys.setrecursionlimit(10**6)

def recur(a, b):
    ret = False

    if dp[a][b] != -1:
        return dp[a][b]

    for i in range(3):
        if a >= arr[i]:
            if not recur(a - arr[i], b):
                ret = True
        if b >= arr[i]:
            if not recur(a, b - arr[i]):
                ret = True

    dp[a][b] = ret
    return ret

arr = list(map(int,input().split()))
dp = [[-1 for i in range(510)] for j in range(510)]

for i in range(5):
    a, b = map(int,input().split())

    if recur(a, b):
        print('A')
    else:
        print('B')

#--------------------------------------------------#
# 메모이제이션
arr = list(map(int,input().split()))
dp = [[-1 for i in range(510)] for j in range(510)]

for _ in range(5):
    a, b = map(int,input().split())

    for i in range(a + 1):
        for j in range(b + 1):
            dp[i][j] = False
            for k in range(3):
                if i >= arr[k] and not dp[i - arr[k]][j]:
                    dp[i][j] = True
                if j >= arr[k] and not dp[i][j- arr[k]]:
                    dp[i][j] = True
    if dp[a][b]:
        print('A')
    else:
        print('B')