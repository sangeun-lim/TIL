# 바텀업 방식
t = int(input())
dp = [0 for i in range(1000010)]

dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,1000010):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in range(t):
    n = int(input())
    print(dp[n])

#--------------------------------------------------------#
# 탐다운 방식
dp = [-1 for i in range(1000010)]

def recur(total):
    ret = 0

    if total < 0:
        return 0

    if total == 0:
        return 1

    if dp[total] != -1:
        return dp[total]

    for i in range(1,4):
        ret += recur(total-i)

    dp[total] = ret

    return dp[total]

t = int(input())
for _ in range(t):
    n = int(input())
    print(recur(n))