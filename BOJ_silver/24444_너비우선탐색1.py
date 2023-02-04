from collections import deque
import sys
input = sys.stdin.readline

def bfs(r):
    global cnt
    que = deque([r])
    V[r] = 1
    while que:
        v = que.popleft()
        graph[v].sort()
        for i in graph[v]:
            if V[i] == 0:
                cnt += 1
                V[i] = cnt
                que.append(i)

N,M,R = map(int,input().split()) # 정점의 수, 간선의 수, 시작정점
graph = [[] for _ in range(N+1)]
V = [0] * (N+1)
cnt = 1

# 그래프 생성
for i in range(M):
    u,v = map(int,input().split()) # 정점 u 와 정점 v
    graph[u].append(v)
    graph[v].append(u)

bfs(R)
for visit in V[1:]:
    print(visit)
