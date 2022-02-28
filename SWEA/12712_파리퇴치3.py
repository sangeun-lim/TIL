T = int(input())
for tc in range(1,T+1):
    N, M= map(int,input().split())
    fly_list = [list(map(int,input().split())) for _ in range(N)]

    max_fly = 0
        # 우 , 하 , 좌 , 상
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 좌상, 우상, 좌하, 우하
    dii = [-1,-1,1,1]
    djj = [-1,1,-1,1]

    for i in range(N):          # 최대 퇴치 파리수
        for j in range(N):      # 모든 원소에 스프레이
            fly = fly_list[i][j]
            for k in range(4):
                for l in range(1,M):
                    ni = i + di[k] * l
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < N :
                        fly += fly_list[ni][nj]
            if fly > max_fly :
                max_fly = fly


            fly = fly_list[i][j]
            for k in range(4):
                for l in range(1,M):
                    ni = i + dii[k] * l
                    nj = j + djj[k] * l
                    if 0 <= ni < N and 0 <= nj < N :
                        fly += fly_list[ni][nj]
            if fly > max_fly :
                max_fly = fly

    print(f'#{tc} {max_fly}')