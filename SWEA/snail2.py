import sys
sys.stdin = open('input.txt')

T = int(input())

#    우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1 ,0]

for tc in range(1,T+1):
    N = int(input())    #  N x N 행렬

    N_list = [[0 for _ in range(N)] for _ in range(N)] # 출력할 배열을 저장할 리스트

    i = j = 0 # [0][0] 시작
    go = 0 # 방향

    for k in range(1, N*N + 1):
        N_list[i][j] = k # 값 저장

        # 위치 지정
        i += di[go]
        j += dj[go]

        if i < 0 or j < 0 or i >= N or j >= N or N_list[i][j] != 0 : # 범위를 벗어나거나, 이미 값이 있을 때
            i -= di[go]
            j -= dj[go]

            go = (go+1) % 4 # 방향 정하기
            # 다시 위치 지정
            i += di[go]
            j += dj[go]

    print(f'#{tc}')
    for _ in N_list:
        print(' '.join(map(str, _)))
    # for _ in N_list:
    #     print(*_)