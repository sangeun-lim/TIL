N = int(input())
dp = [0] * (N+1)

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])

####################################
N = int(input())
dp = [0] * (1000001)
dp[2] = 1
if N > 2 :
    for i in range(3,N+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])