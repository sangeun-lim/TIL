# 1
# 5
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


#
# di = [0,1,0,-1]
# dj = [1,0,-1,0]

# T = int(input())
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# # di = [0,1,0,-1]
# # dj = [1,0,-1,0]
#
# sum_list = 0
#
# for i in range(N):
#     for j in range(N):
#         for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < N : # 유효한 좌표 인덱스
#                 sum_list += abs(arr[ni][nj] - arr[i][j])
#
# print(sum_list)

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = 0

    for i in range(N):
        for j in range(N):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:  # 유효한 좌표 인덱스
                    sum_list += abs(arr[ni][nj] - arr[i][j])
    print(sum_list)