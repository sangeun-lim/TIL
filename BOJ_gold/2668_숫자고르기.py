n = int(input())
arr =[0] + [int(input()) for _ in range(n)]
visited = [False for i in range(n+1)]

def dfs(cur, start):
    visited[cur] = True

    if arr[cur] == start: # 시작점으로 다시 돌아오면
        return True

    if visited[arr[cur]]: # 다음 정점이 시작점이 아닌데 arr[cur]이 방문이 되어있으면
        return False

    return dfs(arr[cur], start)


cnt = 0
ans = []
for i in range(1,n+1):
    visited = [False for i in range(n+1)] # visited 초기화

    if dfs(i,i) :
        cnt += 1
        ans.append(i)

print(cnt)
for i in ans:
    print(i)