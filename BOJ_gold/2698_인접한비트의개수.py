# 탑다운 풀이
def recur(cur, cnt, prv):
    ret = 0
    if cur == n:
        if cnt == m:
            return 1
        else:
            return 0

    if dp[cur][cnt][prv] != -1:
        return dp[cur][cnt][prv]

    for i in range(2):
        ret += recur(cur + 1, cnt + (prv == 1 and i == 1), i)
        # recur(cur + 1, cnt + (prv * i), i)
    dp[cur][cnt][prv] = ret
    return ret

T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    dp = [[[-1 for i in range(2)] for j in range(101)] for k in range(101)]
    recur(0, 0, 0)

    print(recur(0,0,0))

#-----------------------------------------------------------------------#
# 바텀업 풀이

T = int(input())

for _ in range(T):
    n, m = map(int,input().split())
    dp = [[[0 for i in range(2)] for j in range(101)] for k in range(101)]

    # 기저조건
    for i in range(n):
        for j in range(2):
            if i == m:
                dp[n][i][j] = 1

    # 점화식
    for i in range(n)[::-1]:
        for j in range(n)[::-1]:
            for k in range(2):
                for l in range(2):
                    dp[i][j][k] += dp[i + 1][j + k * l][l]

    print(dp[0][0][0])