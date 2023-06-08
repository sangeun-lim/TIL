# 누적합
# H 를 기준으로 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
s = '#' + input() + '#'
w = [0 for i in range(n+2)] # prefix
e = [0 for i in range(n+2)] # suffix

for i in range(1, n + 1):
    w[i] = w[i - 1] + (s[i] == 'W')

for i in range(1, n + 1)[::-1]:
    e[i] = e[i + 1] + (s[i] == 'E')

ans = 0
for i in range(1, n+1):
    if s[i] == 'H':
        ans += w[i] * (pow(2, e[i], 1000000007) - e[i] - 1)

print(ans % 1000000007)
