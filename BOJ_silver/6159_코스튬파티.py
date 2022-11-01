import sys
input = sys.stdin.readline

N, S = map(int,input().split())

lst = []
cnt = 0

for i in range(N):
    x = int(input())
    lst.append(x)

for i in range(N-1):
    for j in range(i+1, N):
        if lst[i] + lst[j] <= S:
            cnt += 1
print(cnt)

#################################################
import sys
input = sys.stdin.readline

N, S = map(int,input().split())

lst = []
for i in range(N):
    x = int(input())
    lst.append(x)
lst.sort()

s = 0
e = N-1
cnt = 0
while s < e :
    if lst[s] + lst[e] <= S:
        cnt += e-s
        s += 1
    else:
        e -= 1
print(cnt)