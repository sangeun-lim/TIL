n = int(input()) # 노드 번호
m = int(input()) # 간선 개수

v = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n+1)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]: #방문처리 되어있으면
            continue
        dfs(nxt)

dfs(1) # 1번 정점과 연결된 정점들을 모두 방문 처리

cnt = 0
for i in range(n+1): # 연결된 정점의 수 세기
    if visited[i]: #방문처리 되어있으면
        cnt += 1

print(cnt-1) # 자기자신도 포함되어있으므로 하나 뺌

####################################
n = int(input())  # 노드 번호
m = int(input())  # 간선 개수

v = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]
cnt = 0

def dfs(cur):
    global cnt

    visited[cur] = True
    cnt += 1

    for nxt in v[cur]:
        if visited[nxt]:  # 방문처리 되어있으면
            continue
        dfs(nxt)
dfs(1)
print(cnt)