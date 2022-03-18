n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
# dp[3] = 5
# dp[4] = 11

for i in range(3,n+1):
    if i % 2 == 0: # i가 짝수이면
        dp[i] = ((dp[i-1]) * 2 + 1) % 10007
    else : # i가 홀수이면
        dp[i] = ((dp[i-1]) * 2 - 1) % 10007

print(dp[n])