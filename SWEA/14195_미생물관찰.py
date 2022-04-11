def BFS(i,j):
    global A,B,max_v
    p = arr[i][j]
    q = [(i,j)]
    arr[i][j] = '_'
    cnt = 1

    while q:
        x ,y = q.pop(0)

        for k in range(4):
            ni = x + dx[k]
            nj = y + dy[k]

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == p :
                arr[ni][nj] = '_'
                q.append((ni,nj))
                cnt += 1

    if cnt > max_v:
        max_v = cnt

    if p == 'A':
        A += 1
    else:
        B += 1

dx = (0,0,-1,1)
dy = (-1,1,0,0)
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    A = B = max_v = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] != '_':
                BFS(i,j)

    print(f'#{tc} {A} {B} {max_v}')