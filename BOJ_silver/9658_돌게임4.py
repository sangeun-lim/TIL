# 돌게임3 에서 n-1 한 결과를 출력하면됨

n = int(input())
dp = [False for _ in range(1001)]

dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5,n+1):
    if not (dp[i-1] and dp[i-3] and dp[i-4]):
        dp[i] = True
    else:
        dp[i] = False

if dp[n-1]:
    print('SK')
else:
    print('CY')