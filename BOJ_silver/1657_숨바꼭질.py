from collections import deque

n,k = map(int,input().split())
que = deque()
visited = [False for _ in range(200001)]

que.append(n)
visited[n] = True
d = 0
while len(que) > 0 :
    size = len(que)

    for _ in range(size):
        cur = que.popleft()

        if cur == k:
            print(d)
            exit()

        for nxt in [cur-1, cur+1, cur*2]:
            if not (0 <= nxt < 200001) or visited[nxt]:
                continue

            que.append(nxt)
            visited[nxt] = True

    d += 1