import sys
N = int(input())
day_money = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (N+1)

# 뒤에서부터 계산해서 최대 수익을 구함
for i in range(N-1,-1,-1):
    if day_money[i][0] + i > N : # 현재 날짜와 상담기간의 합이 퇴사일을 넘긴다면 == 상담을 할 수 없다면
        dp[i] = dp[i+1]          # 일을 할 수 없으므로 다음날의 값이 오늘의 값
    else :                       # 상담을 할 수 있다면
        dp[i] = max(dp[i+1], day_money[i][1] + dp[i + day_money[i][0]]) # 상담을 했을 때와, 안했을때의 값 중 큰 값을 고름

print(dp[0])