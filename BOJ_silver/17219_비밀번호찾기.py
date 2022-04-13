# 82%에서 시간초과
N, M = map(int,input().split())
arr = [list(input().split()) for _ in range(N)]
arr2 = [input() for _ in range(M)]

for j in arr2:
    for i in range(len(arr)):
        if arr[i][0] == j :
            print(arr[i][1])

#############################################

import sys
N, M = map(int,input().split())
ans = {}

for i in range(N):
    web, pw = sys.stdin.readline().strip().split()
    ans[web] = pw

for j in range(M):
    print(ans[sys.stdin.readline().strip()])