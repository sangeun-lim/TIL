import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
v = [[] for i in range(n + 1)]
par = [0 for i in range(n + 1)]

for i in range(n-1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

def dfs(cur, prv):
    par[cur] = prv

    for nxt in v[cur]:
        if nxt == prv:
            continue

        dfs(nxt,cur)

dfs(1,-1)
for i in range(2, n+1):
    print(par[i])
