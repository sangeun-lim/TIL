import sys
sys.setrecursionlimit(10000)

def cycle(x):
    visited[x] = 1 # 방문한곳 1로 초기화
    next = arr[x]  # 이어진 수의 다음 방문지로
    if visited[next] == 0:
        cycle(next)

T = int(input())
for tc in range(T):
    N = int(input())                                # 정수의 개수
    arr = [0] + list(map(int,input().split()))
    visited = [0] * (N+1)
    cnt = 0

    for i in range(1,N+1):
        if visited[i] == 0 :                        # 방문하지 않은 정점이면
            cycle(i)
            cnt += 1
    print(cnt)

######################################################

T = int(input())

def bfs(x):
    queue = [x]
    visited[x] = 1
    while queue:
        v = queue[0]
        queue.pop(0)
        next = arr[v]
        if visited[next] == 0 :
            visited[next] = 1
            queue.append(next)
    return True

for i in range(T):
    cnt = 0
    N = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [0] * (N+1)

    for i in range(1,N+1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1

    print(cnt)

