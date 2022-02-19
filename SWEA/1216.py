import sys
sys.stdin = open('input.txt')

# for tc in range(10):
#     n = input()
#     board = [input()for _ in range(100)]
#
#     max_V = 0
#
#     # 가장 긴걸 발견하는 순간 종료
#     for i in range(100,0,-1):
#         for j in range(100):
#             row_list = []
#             for k in range(100):
#                 if k + i < 100:
#                     row_list.append(board[i][k+j])
#                     if row_list == row_list[::-1]:
#                         V = len(row_list)
#             if max_V < V :
#                 max_V = V
#     # 전치
#     # for 문 두개 돌리면서 i,j 바뀌면서
#     #
#
#     for i in range(100,0,-1):
#         for j in range(100):
#             col_list = []
#             for k in range(100):
#                 if k + i < 100:
#                     col_list.append(board[k+i][j])
#                     if col_list == col_list[::-1]:
#                         V = len(col_list)
#             if max_V < V :
#                 max_V = V
#
#     print(f'#{tc+1} {max_V}')
####################################################################
def palindrome(arr):
    for i in range(100,0,-1):
        if max_V >= i :
            break
        for j in range(100):
            for k in range(100-i+1):
                if arr[j][k:k+i] == arr[j][k:k+i][::-1]:
                    V = len(arr[j][k:k+i])
                    if V > max_V :
                        max_V = V
    return max_V

for tc in range(10):
    n = input()
    board = [input()for _ in range(100)]       # 100 x 100 배열 입력 받기

    max_V = palindrome(board)   # 가장 긴 회문의 길이
    board2 = list(map(list, zip(*board)))
    max_V2 = palindrome(board2)
    real_max = 0

    if max_V > max_V2 :
        real_max = max_V
    else :
        real_max = max_V2
    print(f'#{tc + 1} {real_max}')

    # for i in range(100,0,-1):
    #     if max_V >= i :
    #         break
    #     for j in range(100):
    #         for k in range(100-i+1):
    #             if board[j][k:k+i] == board[j][k:k+i][::-1]:
    #                 V = len(board[j][k:k+i])
    #                 if V > max_V :
    #                     max_V = V
    #
    # for i in range(100,0,-1):
    #     if max_V >= i :
    #         break
    #     for j in range(100-i+1):
    #         for k in range(100):
    #             col_list = []
    #             for l in range(i):
    #                 col_list.append(board[l+j][k])
    #             if col_list == col_list[::-1]:
    #                 V = len(col_list)
    #             if V > max_V:
    #                 max_V = V
    # print(f'#{tc + 1} {real_max}')

    # 전치 사용해서 열 >> 행으로
    # for 문 두개 돌리면서 i,j 바뀌면서
    # 행에서 쓰던 코드를 그대로 쓸 수 있음