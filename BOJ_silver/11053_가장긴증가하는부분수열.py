n = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    dp[i] = 1 #시작
    for j in range(i):
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

