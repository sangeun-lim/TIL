# 가장 큰 값 < 나머지 전체 합 ==> 가장 큰 값 + 나머지 전체합이 홀수면 1 , 짝수면 0

import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(max(arr))
else:
    total = sum(arr)
    x = max(arr)
    y = total - x

    if x >= y:
        print(x-y)
    else:
        if total % 2:
            print(1)
        else:
            print(0)