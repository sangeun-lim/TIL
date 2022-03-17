T = int(input())
for tc in range(T):
    n = int(input())
    dp = [0 for i in range(1000000)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,1000000):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

    print(dp[n])
# pypy3 으로 하면 시간초과 안남


##################################################
T = int(input())

def recur(total):
    global cnt

    if total > n:
        return

    if total == n:
        cnt += 1
        return

    for i in range(1, 4):
        recur(total + i)

dp = [-1 for i in range(1000010)]

for tc in range(T):
    n = int(input())
    cnt = 0
    recur(0)
    print(cnt)

###############################
def f(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 4
    else:
        return f(x-1)+f(x-2)+f(x-3)

x=int(input())

for i in range(x):
    print(f(int(input())))