from collections import deque

def BFS():

    day = -1
    while queue:
        for i in range(len(queue)):
            z, x, y = queue.popleft()
            for j in range(6):
                nz = z + dz[j]
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = 1
                    queue.append((nz,nx,ny))
        day += 1

    # 익지않은 토마토 확인
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1
    return day

M,N,H = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)] # 3차원 배열
# 우, 하 , 좌, 상, 위, 아래
dx = [0,1,0,-1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:  # 익은 토마토이면 queue에 저장
                queue.append((i, j, k))

print(BFS())

#################################################################

from collections import deque

def BFS():
    while queue:
        for i in range(len(queue)):
            z, x, y = queue.popleft()
            for j in range(6):
                nz = z + dz[j]
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz, nx, ny))

# 익지않은 토마토 확인 및 결과
def result():
    day = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    return -1
                day = max(day,box[i][j][k])
    return day-1


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]  # 3차원 배열
# 우, 하 , 좌, 상, 위, 아래
dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:  # 익은 토마토이면 queue에 저장
                queue.append((i, j, k))
BFS()
print(result())