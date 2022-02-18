import sys
sys.stdin = open('input.txt')

# for tc in range(10):
#     N = int(input()) # 테스트 케이스의 번호
#     ladder = [list(map(int, input().split())) for _ in range(100)] # 사다리 저장
#     #    하, 우, 좌
#     di = [1,0,0]
#     dj = [0,1,-1]
#
#     M = len(ladder)
#     i = j = 0  # [0][0] 시작
#     d = 0  # 방향
#
#     # 첫번째 행의 열들만 확인하면 됨
#
#
#     while ladder[99][j] != 2:
#         # 범위 벗어나면 안됨
#         # 이미 값이 있어도 안됨
#         # 방향 바꾸고 움직여야 됨
#         if i < 0 or j < 0 or i >= N or j >= N or N_list[i][j] != 0:
#
#         # 오른쪽이 1이면 그 방향으로 진행
#         if ladder[i][j+1] == 1 :
#
#         # 왼쪽이 1 이면 그 방향으로 진행
#         elif ladder[i][j-1] == 1 :
#
#         # 아니라면 계속 밑으로 진행
#         if ladder[i][j] == 1 :
#             i += di[d]
#             j += dj[d]

for tc in range(1,11):
    N = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]

    # 도착지에서 출발

    for i in range(100):
        if ladder[99][i] == 2 :
            X = i # 출발지점
            break # 찾으면 멈춤

    Y = 99

    while True:
        # 왼쪽으로 갈 수 있을 때
        if X > 0 and ladder[Y][X-1]:
            # 최대한 왼쪽으로 감
            while X > 0 and ladder[Y][X-1]:
                X -= 1
            # 0이 나오면 위로 올라감
            else :
                Y -= 1
        # 오른쪽으로 갈 수 있을 때
        elif X < 99 and ladder[Y][X+1]:
            # 최대한 오른쪽으로 감
            while X < 99 and ladder[Y][X+1]:
                X += 1
            # 0이 나오면 위로 올라감
            else :
                Y -= 1
        # 위로만 갈수 있을 때
        else:
            Y -= 1
        # 꼭대기에 도착하면
        if Y == 0:
            break

    print(f'#{N} {X}')
###########################################################
for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    start_list = [0] * 100       # 시작점을 담아줄 리스트

    # 0행에서 시작점들 모두 찾아주기
    for i in range(100):
        if ladder[0][i] == 1 :
            start_list[i] = 1

    #    하, 우, 좌
    di = [1, 0, 0]
    dj = [0, 1, -1]
    d = 0

    for i in range(100):
        x = i
        y = 0
        if start_list[x] == 1 :
            while y < 0:
                # 오른쪽이 1 이고 왼쪽이 0 이고 아래가 1 이면 오른쪽으로
                if ladder[x][y+1] == 1 and ladder[x][y-1] == 0 :
                    while ladder[i][y+1] == 1 and ladder[i][y-1] == 0 :
                        y += 1
                    else :
                        x += 1
                # 왼쪽이 1이고 오른쪽이 0 이고, 아래가 1이면 왼쪽으로
                elif ladder[x][y-1] == 1 and ladder[x][y+1] == 0 :
                    while ladder[x][y-1] == 1 and ladder[x][y+1] == 0 :
                        y -= 1
                    else :
                        x += 1
                # 왼쪽, 오른쪽 둘다 0 이면 아래쪽으로
                else :
                    x += 1

        print(f'#{N} {i}')
