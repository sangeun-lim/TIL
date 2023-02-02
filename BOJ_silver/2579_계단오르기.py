import sys
input = sys.stdin.readline

N = int(input()) # 계단의 개수
stairs = [int(input()) for i in range(N)] # 각 계단별 점수
dp = [0] * 301

# if N == 1 :
#     print(stairs[0])
# elif N == 2 :
#     print(stairs[0] + stairs[1])
# elif N == 3 :
#     print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
if len(stairs) <= 2 :
    print(sum(stairs))
else:
    dp[0] = stairs[0]  # 1번째 계단까지의 최대값
    dp[1] = stairs[0] + stairs[1]  # 2번째 계단까지의 최대값
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])  # 3번째 계단까지의 최대값

    for i in range(3,N):
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    print(dp[N-1])

