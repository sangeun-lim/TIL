def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in tree[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True
    que = [n]
    while que:
        v = que.pop(0)
        print(v, end= ' ')
        for i in tree[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

N,M,V = map(int,input().split())
tree = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(1,N+1):
    tree[i].sort()

dfs(V)

visited = [False] * (N+1)
print()
bfs(V)

############################################
N, M, V = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    m1,m2 = map(int,input().split())
    graph[m1][m2] = graph[m2][m1] = 1

def bfs(n):
    que = [n]
    visited[n] = True

    while que :
        v = que.pop(0)
        print(v, end=' ')
        for w in range(len(graph[v])):
            if graph[v][w] == 1 and not visited[w]:
                visited[w] = True
                que.append(w)

def dfs(n):
    print(n, end = ' ')
    visited[n] = True

    for w in range(len(graph[n])):
        if graph[n][w] == 1 and not visited[w]:
            dfs(w)

dfs(V)
visited = [False] * (N+1)
print()
bfs(V)


