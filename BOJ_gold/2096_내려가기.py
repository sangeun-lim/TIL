import sys
input = sys.stdin.readline

n = int(input())
dp1 = [[0,0,0], [0,0,0]]
dp2 = [[0,0,0], [0,0,0]]
idx = 0

for i in range(n):
    arr = list(map(int,input().split()))

    for j in range(3):
        dp1[idx][j] = 0
        dp2[idx][j] = 999999

        for k in range(3):
            if abs(j-k) >= 2:
                continue

            dp1[idx][j] = max(dp1[idx][j], dp1[idx ^ 1][k] + arr[j])
            dp2[idx][j] = min(dp2[idx][j], dp2[idx ^ 1][k] + arr[j])

    idx ^= 1

print(max(dp1[idx ^ 1]), min(dp2[idx ^ 1]))
