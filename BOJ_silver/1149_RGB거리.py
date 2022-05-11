N = int(input())

arr = [[0 for i in range(3)]] + [list(map(int,input().split())) for i in range(N)]
dp = [[0 for i in range(3)] for j in range(N+1)]


for i in range(1,N+1):
    for j in range(3):
        mn = 100000000
        for k in range(3):
            if j == k :
                continue

            mn = min(mn, dp[i-1][k])
        dp[i][j] = mn + arr[i][j]

print(min(dp[N]))

################################################################
N = int(input())

arr = [[0 for i in range(3)]] + [list(map(int,input().split())) for i in range(N)]
dp = [[0 for i in range(3)] for j in range(N+1)]


for i in range(1,N+1):
    mn = 10000000
    minx = 0

    # 이전줄에서 제일 작은 값 찾기
    for j in range(3):
        if mn > dp[i-1][j]:
            mn = dp[i-1][j]
            midx = j

    for j in range(3):
        if j == midx:
            continue
        dp[i][j] = mn + arr[i][j]

    mn = 10000000
    for j in range(3):
        if j == midx:
            continue

        mn = min(mn,dp[i-1][j])
    dp[i][midx] = mn + arr[i][midx]
print(min(dp[N]))