import sys

N = int(input())
xy = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

xy.sort(key=lambda x : (x[1],x[0]))

for i in range(N):
    print(*xy[i])
