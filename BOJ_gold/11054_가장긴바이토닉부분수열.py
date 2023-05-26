n = int(input())
arr = list(map(int,input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

dp2 = [1 for i in range(n)]
for i in range(n)[::-1]:
    for j in range(i)[::-1]:
        if arr[j] > arr[i]:
            dp2[j] = max(dp2[j], dp2[i]+1)

for i in range(n):
    dp[i] += dp2[i]

print(max(dp)-1)