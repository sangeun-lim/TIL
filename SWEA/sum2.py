# 부분집합의 합이 0이 되는 것이 존재하는지 계산

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    n = len(arr)

    for i in range(1, 1<<n):                            # 공집합을 제외한 모든 부분집합의 개수만큼 순회하는 반복
        total = 0
        for j in range(n):                              # 리스트의 요소가 부분집합에 포함되어 있는지 하나하나 확인하기 위한 반복
            if i & (1<<j):                              # i는 부분집합에 들어간 요소
                                                        # 1이 j만큼씩 이동하면서 i와 비교하여 부분집합에 포함된 요소인지 여부 확인
                total += arr[j]
        if total == 0 :
            ans = True
            break
    else :
        ans = False

    print(f'{tc+1} {ans}')