import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()

    res = 1
    score = arr[0][1]

    for i in range(1,n):
        if arr[i][1] < score:
            res += 1
            score = arr[i][1]
    print(res)
