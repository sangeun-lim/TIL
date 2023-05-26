import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().split())
k = int(input())
v = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())

    v[a].append([b,c])

dist = [1000000000 for i in range(n+1)]

pq = [] # 우선순위 큐

dist[k] = 0 #거리의 시작점은 0
heapq.heappush(pq, (0, k)) # 거리와 노드 push

while len(pq) > 0:
    # mn = 100000000
    # cur = 0
    # for i in range(1, n+1):
    #     if not visited[i] and dist[i] < mn:
    #         mn = dist[i]
    #         cur = i
    d, cur = heapq.heappop(pq)

    # if visited[cur]:
    #     continue
    #
    # visited[cur] = True

    if dist[cur] != d: # 이미 거리의 최소값이 들어갔다는 의미
        continue

    for i in range(len(v[cur])):
        nxt = v[cur][i][0]
        nd = dist[cur] + v[cur][i][1]

        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, n+1):
    if dist[i] == 1000000000:
        print('INF')
    else:
        print(dist[i])