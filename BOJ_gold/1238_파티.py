# 정방향에서 다익스트라 한번
# 역방향에서 다익스트라 한번해서 값 구하기

import heapq

n, m, x = map(int,input().split())
v = [[] for _ in range(n+1)]   # 정방향 그래프
rv = [[] for _ in range(n+1)]  # 역방향 그래프

for i in range(m):
    a, b, c = map(int,input().split())

    v[a].append([b,c])
    rv[b].append([a,c])

def get_dist(s, v): # 시작노드와 그래프
    pq = []
    dist[s] = 0

    heapq.heappush(pq, (0, s))

    while pq:
        d, cur = heapq.heappop(pq)

        if dist[cur] != d: # 방문처리랑 동치
            continue

        for i in range(len(v[cur])):
            nxt = v[cur][i][0]    # 다음 노드
            nd = d + v[cur][i][1] # 현재까지 노드의 거리 + 다음 거리

            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))

dist = [1000000000 for _ in range(n+1)]
get_dist(x,v)
ans = dist.copy()

dist = [1000000000 for _ in range(n+1)]
get_dist(x,rv)

for i in range(1, n+1):
    ans[i] += dist[i]

mx = -1
for i in range(1, n+1):
    mx = max(mx, ans[i])

print(mx)