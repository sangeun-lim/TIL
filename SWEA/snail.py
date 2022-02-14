# 5
# 9 20 2 18 11
# 19 1 25 3 21
# 8 24 10 17 7
# 15 4 16 5 6
# 12 13 22 23 14

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

my_list = [[0]*N for _ in range(N)]
#    우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]

i = j = 0 # [0][0] 시작
d = 0 # 방향

for k in range(1,N*N+1):
    my_list[i][j] = k

    i += di[d]
    j += dj[d]

    if i < 0 or j < 0 or i >= N or j >= N or my_list[i][j] != 0 :
        i -= di[d]
        j -= dj[d]

        d = (d+1) % 4

        i += di[d]
        j += dj[d]

for _ in my_list:
    print(*_)
