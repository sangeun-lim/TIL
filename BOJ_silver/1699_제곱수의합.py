# 탐다운 방식
n = int(input())
dp = [-1 for _ in range(100010)]

def recur(total):
    if total == n:
        return 0

    if dp[total] != -1:
        return dp[total]

    ret = 100000
    for i in range(1,n+1):
        if i * i > n - total:
            break

        ret = min(ret, recur(total + i * i) + 1)

    dp[total] = ret

    return dp[total]

print(recur(0))

#--------------------------------------------------#
# 바텀업 방식
# pypy3로 제출
import sys
input = sys.stdin.readline

n = int(input())
dp = [100000 for _ in range(n+1)]

dp[0] = 0
for i in range(1,n+1): # 1 ~ n개의 배열에 최소개수 채우기
    for j in range(1,n+1):
        if j * j > i:
            break
        dp[i] = min(dp[i], dp[i - j * j] +1)

print(dp[n])