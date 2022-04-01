import sys
sys.stdin=open('sample_input.txt')
from collections import deque

T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    que = deque()
    visited = [False for _ in range(1000001)]   # 최대 가능한 연산까지

    que.append(n)
    visited[n] = True
    d = 0                                       # 연산횟수

    while que:                                  # bfs 부분
        size = len(que)                         # que의 크기만큼
        for _ in range(size):
            cur = que.popleft()

            if cur == k :
                print(f'#{tc} {d}')

            for nxt in [cur+1, cur-1, cur*2, cur-10]:           # 사용할수 있는 연산
                if not(0 <= nxt < 1000001) or visited[nxt] :    # 연산의 중간결과도 항상 백만이하의 자연수이여야 함
                    continue
                que.append(nxt)
                visited[nxt] = True
        d += 1
