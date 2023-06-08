import sys
input = sys.stdin.readline

n = int(input())
res_x = []
res_y = []
for i in range(n):
    x,y = map(int,input().split())
    res_x.append(x)
    res_y.append(y)
res_x.sort()
res_y.sort()

total = 0
if n % 2: # 고객수가 홀수면
    x = res_x[n//2]
    y = res_y[n//2]
    for i in range(n):
        total += abs(res_x[i] - x) + abs(res_y[i] - y)

else:
    x = res_x[n // 2 - 1]
    y = res_y[n // 2 - 1]
    for i in range(n):
        total += abs(res_x[i] - x) + abs(res_y[i] - y)

print(total)