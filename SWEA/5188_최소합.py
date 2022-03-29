import sys
sys.stdin=open('sample_input.txt')

def BFS(x,y):
    global min_total , sub_total    # 최소합, 부분합
    if min_total < sub_total :      # 최소합보다 부분합의 크면 return
        return

    if x == N-1 and y == N-1:       # 맨 마지막 칸에 도착했을때
        if min_total > sub_total:   # 최소합 갱신
            min_total = sub_total

    for l in range(2):              # 우, 하 방향으로만 움직이므로
        ni = x + dx[l]
        nj = y + dy[l]
        # if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]: # 범위를 벗어나지 않고, 방문하지 않았을때
        if 0 <= ni < N and 0 <= nj < N:  # 범위를 벗어나지 않고
            sub_total += arr[ni][nj] # 최소합 합산
            # visited[ni][nj] = True   # 방문표시
            BFS(ni,nj)
            sub_total -= arr[ni][nj] # 합산한 값 이전으로
            # visited[ni][nj] = False  # 방문한 곳 초기화

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]    # 숫자판
    # visited = [[False] * N for _ in range(N)]                   # 방문여부
    min_total = 999999      # 최소합
    sub_total = arr[0][0]   # 부분합

    # 우, 하
    dx = [0,1]
    dy = [1,0]

    BFS(0,0)                # 시작지점이 (0,0)
    print(f'#{tc} {min_total}')