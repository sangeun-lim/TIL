# 방문여부를 체크하는 버전 ( 땅은 그대로 둠 )
import sys
sys.setrecursionlimit(10000)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DFS(x,y):
    check[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) and (0 <= ny < M):
            if area[nx][ny] == 1 and check[nx][ny] == False:
                check[nx][ny] = True
                DFS(nx,ny)

T = int(input())
for tc in range(T):
    M,N,K = map(int,input().split())
    area = [[0 for _ in range(M)] for _ in range(N)] # 땅 초기화
    check =[[False] * M for _ in range(N)] # 방문여부

    # 땅에 배추 심기
    for j in range(K):
        X,Y = map(int,input().split())
        area[Y][X] = 1

    cnt = 0 # 배추흰지렁이 수
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1 and check[i][j] == False:
                DFS(i,j)
                cnt += 1
    print(cnt)

#################################################################
# 방문한 땅을 0으로 만드는 버전
import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                dfs(nx, ny)


t = int(input())
for _ in range(t):
    n, m, c = map(int, input().split())
    ans = 0
    board = [[0] * n for k in range(m)]
    for i in range(c):
        a, b = map(int, input().split())
        board[b][a] = 1
    for p in range(m):
        for q in range(n):
            if board[p][q] == 1:
                dfs(p, q)
                ans += 1
    print(ans)