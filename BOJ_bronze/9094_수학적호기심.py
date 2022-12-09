import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    cnt = 0
    for a in range(1,n-1):
        for b in range(a+1,n):
            x = float((a**2 + b**2 + m) / (a*b)).is_integer()
            if x:
                cnt += 1
    print(cnt)

#############################
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    cnt = 0
    for a in range(1,n-1):
        for b in range(a+1,n):
            if (a**2 + b**2 + m) % (a * b) == 0:
                cnt += 1
    print(cnt)
#####################################
import sys
input = sys.stdin.readline

result = [[0 for _ in range(101)] for _ in range(101)]
for b in range(2, 100):
    for m in range(1, 101):
        result[b][m] = result[b - 1][m]
        for a in range(1, b):
            if (a * a + b * b + m) % (a * b) == 0:
                result[b][m] += 1

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(result[n - 1][m])