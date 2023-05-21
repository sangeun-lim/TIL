import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
n, r, q = map(int,input().split())
v = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())

    v[a].append(b)
    v[b].append(a)

sz = [0 for i in range(n+1)]

def dfs(cur, prv):
    sz[cur] = 1

    for nxt in v[cur]:
        if nxt == prv:
            continue

        sz[cur] += dfs(nxt,cur)
    return sz[cur]

dfs(r, -1)

for i in range(q):
    x = int(input())

    print(sz[x])
