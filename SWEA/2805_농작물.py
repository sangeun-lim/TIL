# T = int(input()) # 테스트 케이스 개수
#
# for tc in range(T):
#     N = int(input()) # 농장의 크기
#     farm = [list(map(int,input())) for _ in range(N)]
#     money = 0
#
#     middle = N // 2
#
#     # for i in range(N):
#     #     if i == N // 2 : # i == 3
#     #         for j in range(N):
#     #             money += farm[i][j]
#     #     elif i < N // 2:  # i == 0 , 1, 2 , j == 3, 234 ,12345
#     #         for j in range(middle):
#     #             money += farm[i][j]
#     #
#     #     else :          # i == 4, 5, 6 , j == 12345,234,3
#     #         for j in range(middle):
#     #             money += farm[i][j]
#     #
#     # print(money)
#
#     left = N//2
#     right = N//2
#     for i in range(N):
#         if i == 0 :
#             continue
#         elif i <= middle :      # 중간 행까지는 열의 범위를 넓힘
#             left -= 1
#             right += 1
#         else :                  # 중간 행 이후로는 열의 범위로 좁힘
#             left += 1
#             right -= 1
#         for j in range(left,right+1):
#             money += farm[i][j]
#     print(f'#{tc+1} {money}')
#
# ##############################################################
# T = int(input())
#
# for tc in range(1, 1 + T):
#
#     # 농장의 크기
#     n = int(input())
#
#     # 농장
#     farm = [list(map(int, input())) for _ in range(n)]
#
#     # 결과
#     money = 0
#     mid = n//2
#     # 3가지 경우의 수
#     # 1. 0~n//2까지
#     for i in range(0, mid):
#         for j in range(i + 1):
#             if j == 0:
#                 money += farm[i][mid]
#
#             else:
#                 money += farm[i][mid + j]
#                 money += farm[i][mid - j]
#
#     # 2. n//2
#     for j in range(n):
#         money += farm[mid][j]
#
#     # 3. n//2+1 ~ n까지
#     for i in range(mid + 1, n):
#         for j in range(n - i):
#             if j == 0:
#                 money += farm[i][mid]
#
#             else:
#                 money += farm[i][mid + j]
#                 money += farm[i][mid - j]
#
#     print(f'#{tc+1} {money}')

###########################################################################
import sys
sys.stdin=open('input.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    total = 0

    arr = [list(map(int,input())) for _ in range(N)]
    mid = N//2
    for i in range(mid+1):
        for j in range(mid-i, mid+i+1):
            if i == mid:                # 중앙줄 계산
                total += arr[i][j]
            else:
                total += arr[i][j]      # 첫줄에서 한줄씩 아래로
                total += arr[N-1-i][j]  # 끝줄에서 한줄씩 위로

    print(f'#{tc} {total}')