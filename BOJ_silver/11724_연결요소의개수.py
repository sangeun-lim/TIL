import sys
sys.setrecursionlimit(10000)

n, m = map(int,sys.stdin.readline().split())
v = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

visited = [False] *(n+1)
def dfs(cur): # 시작정점과 연결된 노드들을 모두 방문처리 해주는 함수
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)

cnt = 0
for i in range(1,n+1): # 1번노드부터 n번노드까지
    if not visited[i]: # 방문처리가 안되어있으면
        cnt += 1       # 새로운 연결요소 라는 의미이므로
        dfs(i)
print(cnt)