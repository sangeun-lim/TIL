from collections import deque
import sys

n, m = map(int,sys.stdin.readline().strip().split())
arr = [sys.stdin.readline().strip() for _ in range(n)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]


def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(x,y):
    que = deque()
    visited = [[False for _ in range(m)] for j in range(n)]
    
    d = 0
    que.append([x,y])
    visited[x][y] = True

    while que:
        size = len(que)
        for _ in range(size):
            x, y = que.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not in_range(nx,ny) or visited[nx][ny] or arr[nx][ny] != 'L':
                    continue

                que.append([nx,ny])
                visited[nx][ny] = True
        d += 1

    return d -1 

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i,j))

print(ans)