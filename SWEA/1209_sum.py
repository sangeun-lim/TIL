import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    c1 = c2 = 0
    for i in range(100):
        c1 += arr[i][i]               # 대각선 합         # 좌상단 -> 우하단
        c2 += arr[i][99-i]            # 엇대각선 합       # 우상단 -> 좌하단
    max_sum = c1 if c1 > c2 else c2

    for i in range(100):
        c3 = c4 = 0
        for j in range(100):
            c3 += arr[i][j]           # 행 합
            c4 += arr[j][i]           # 열 합
        if c3 > max_sum :
            max_sum = c3
        if c4 > max_sum:
            max_sum = c4

    print(f'#{tc} {max_sum}')