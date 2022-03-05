N = int(input())
arr = list(map(int,input().split()))
arr2 = [0 for i in range(N)]
visited = [False for i in range(N)]
ans = 0

def recur(cur):
    global ans
    #기저조건
    if cur == N:
        total = 0
        for i in range(1,N):
            # total += abs(arr[arr2[i]] - arr[arr2[i-1]])
            total += abs(arr2[i] - arr2[i-1])
        ans = max(ans,total)
        return

    # 재귀 호출
    for i in range(N):
        if visited[i]:
            continue

        # arr2[cur] = i
        arr2[cur] = arr[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)

print(ans)