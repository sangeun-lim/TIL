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

def dfs2(cur):
    visited[cur] = True

    for nxt in v[cur]:
        if visited[nxt]:
            continue

        dfs2(nxt)

T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    v = [[] for i in range(n + 1)]
    visited = [False for i in range(n+1)]
    st = []

    for i in range(m):
        a,b = map(int,input().split())
        v[a].append(b)

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    cnt = 0
    visited = [False for i in range(n+1)]
    while st:
        if not visited[st[-1]]:
            dfs2(st[-1])
            cnt += 1

        st.pop()

    print(cnt)