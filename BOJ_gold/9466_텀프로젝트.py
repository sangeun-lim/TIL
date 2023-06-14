import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    if cycle[cur] != -1:
        return -1

    if visited[cur]:
        return cur

    visited[cur] = True

    ret = dfs(arr[cur])

    if ret == -1:
        cycle[cur] = 0
        return -1

    cycle[cur] = 1
    if cur == ret:
        ret = -1

    return ret

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [False for i in range(n+1)]
    cycle = [-1 for i in range(n+1)]

    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    cnt = 0
    for i in range(1,n+1):
        if cycle[i] == 0:
            cnt += 1

    print(cnt)