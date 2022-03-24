n = int(input())
arr = [input() for _ in range(n)]
visited = [[False for i in range(n)] for j in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 원래는 노드 하나 => 정수 하나로 표현
# 노드 하나 => 정수 두개로 표현 ( 좌표로 )

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):  # 2차원 dfs 돌리는법
    ret = 1
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] != '1': # 방문했거나, 범위를 벗어나거나
            continue

        # if not in_range(nx,ny) or visited[nx][ny]:
        #     continue

        ret += dfs(nx,ny) # 리턴 값 누적
    return ret

# 연결노드의 개수 구하기
# 각 연결노드의 크기 구하기
cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or arr[i][j] == '0':
            continue

        cnt += 1
        ans.append(dfs(i,j))

ans.sort()
print(cnt)
for i in ans:
    print(i)

