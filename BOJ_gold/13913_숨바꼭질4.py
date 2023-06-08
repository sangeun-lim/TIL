from collections import deque

n, m = map(int,input().split())
que = deque()
visited = [False for i in range(200010)]
prv = [-1 for i in range(200010)]

d = 0
visited[n] = True
que.append(n)

while que:
    size = len(que)
    for _ in range(size):
        cur = que[0]
        que.popleft()

        if cur == m:
            print(d)
            break

        for nxt in [cur-1, cur+1, 2*cur]:
            if not (0 <= nxt < 200010) or visited[nxt]:
                continue

            que.append(nxt)
            visited[nxt] = True
            prv[nxt] = cur

    d += 1

cur = m
ans = []
while cur != -1:
    ans.append(cur)
    cur = prv[cur]

print(*ans[::-1])