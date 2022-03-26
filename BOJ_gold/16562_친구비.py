import sys
sys.setrecursionlimit(100000)

n, m, k = map(int,sys.stdin.readline().split())
arr = [0] + list(map(int,sys.stdin.readline().split()))
v = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    v[a].append(b)
    v[b].append(a)

visited = [False] * (n+1)

def dfs(cur):
    money = arr[cur]
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue
        money = min(money,dfs(nxt))

    return money

total = 0
for i in range(1,n+1):
    if visited[i] :
        continue
    total += dfs(i)

if k >= total:
    print(total)
else :
    print('Oh no')