
def bfs(ci,cj):
    queue = [(ci,cj)]
    arr[ci][cj] = 1

    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1:
                queue.append((ni,nj))
                arr[ni][nj] = arr[x][y] + 1
    return

n, m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]
di = [-1,1,0,0]
dj = [0,0,-1,1]
bfs(0,0)

print(arr[n-1][m-1])
