import sys
sys.stdin = open('input.txt')

T = int(input())

#    우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]

for tc in range(1,T+1):
    N = int(input())    #  N x N 행렬

    N_list = [[0 for _ in range(N)] for _ in range(N)]

    i = j = 0 # [0][0] 시작
    d = 0 # 방향

    for k in range(1,N*N + 1):
        N_list[i][j] = k
        i += di[d]
        j += dj[d]

        # 범위 벗어나면 안됨
        # 이미 값이 있어도 안됨
        # 방향 바꾸고 움직여야 됨
        if i < 0 or j < 0 or i >= N or j >= N or N_list[i][j] != 0 :
            i -= di[d]
            j -= dj[d]

            d = (d+1) % 4

            i += di[d]
            j += dj[d]
    print(f'#{tc}')
    for _ in N_list:
        print(*_)







