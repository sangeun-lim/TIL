n, m = map(int,input().split())
x, y, d = map(int,input().split()) # 현재 좌표 와 방향
arr = [list(map(int,input().split())) for _ in range(n)]

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0
while True:
    if arr[x][y] == 0: # 후진한 칸이 0일 때만
        cnt += 1

    arr[x][y] = 2

    flag = False
    for i in range(4):
        d = (d + 3) % 4 # 좌회전

        nx = x + dx[d]
        ny = y + dy[d]

        # 갈 수 있는 곳이 있다면
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0: # 회전 하지 못하게
            flag = True
            break

    if flag: # 그 방향으로 이동
        x += dx[d]
        y += dy[d]
    else: # 청소되지 않은 빈 칸이 없는 경우, 반대방향으로(후진)
        nx = x - dx[d]
        ny = y - dy[d]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 2:
            x = nx
            y = ny
        else: # 그 위치가 벽이라면
            break
print(cnt)