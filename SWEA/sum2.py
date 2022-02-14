# 부분집합의 합이 0이 되는 것이 존재하는지 계산

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    n = len(arr)

    for i in range(1, 1<<n): # 부분집합의 개수 만큼
        total = 0
        for j in range(n):
            if i & (1<<j):
                total += arr[j]
        if total == 0 :
            ans = True
            break
    else :
        ans = False

    print(f'{tc+1} {ans}')