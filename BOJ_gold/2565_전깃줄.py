# 왼쪽 값 기준으로 정렬해주고
# 오른쪽 값만 남긴 상태에서 가장 긴 증가하는 부분 수열의 개수를 구하면 됨
# 전체 - 개수 : 정답
# LIS

n = int(input())
arr = sorted([list(map(int,input().split())) for _ in range(n)])
dp = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))