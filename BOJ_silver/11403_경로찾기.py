# 플로이드-와샬 알고리즘 풀이
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[j][i] and arr[i][k]:
                arr[j][k] = 1
for a in arr:
    print(*a)

#---------------------------------------------------------#
# BFS

from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(N)]

    while queue:
        q = queue.popleft()
        for i in range(N):
            if check[i] == 0 and graph[q][i]:
                queue.append(i)
                check[i] = 1
                visited[x][i] =1

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

for i in range(N):
    bfs(i)

for i in visited:
    print(*i)

#---------------------------------------------------------#
# DFS

def dfs(x):
    for i in range(N):
        if graph[x][i] and visited[i] == 0:
            visited[i] = 1
            dfs(i)

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]

for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    visited = [0 for _ in range(N)]