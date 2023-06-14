# 위상정렬 문제
# 코사라주 알고리즘

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs(nxt)

    st.append(cur)

def rdfs(cur, arr):
    visited[cur] = True
    arr.append(cur)
    for nxt in rv[cur]:
        if visited[nxt]:
            continue

        rdfs(nxt, arr)

n, m = map(int,input().split())
v = [[] for i in range(n + 1)]
rv = [[] for _ in range(n + 1)]
visited = [False for i in range(n+1)]
st = []

for i in range(m):
    a,b = map(int,input().split())
    v[a].append(b)
    rv[b].append(a)

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)

result = []
visited = [False for i in range(n+1)]
while st:
    ssc = []
    node = st.pop()
    if not visited[node]:
        rdfs(node,ssc)
        result.append(sorted(ssc))

print(len(result))
answer = sorted(result)
for i in answer:
    print(*i, -1)