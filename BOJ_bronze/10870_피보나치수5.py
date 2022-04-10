n = int(input())
dp = [0] * (21)
dp[0] = 0
dp[1] = 1
if n > 1:
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

#################
fibs = [0, 1]
n = int(input())
for i in range(1, n):
    fibs.append(fibs[i] + fibs[i-1])
print(fibs[n])