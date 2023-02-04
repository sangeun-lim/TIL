from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
day = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]
queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i,j))
while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
            box[ny][nx] = box[y][x] + 1
            if box[ny][nx] - 1 > day:
                day = box[ny][nx] - 1
            queue.append((ny,nx))

# 토마토가 모두 익지 못하는 상황이면 -1 출력
for tomato in box:
    if 0 in tomato:
        day = -1
print(day)
