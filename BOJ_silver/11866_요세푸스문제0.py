N, K = map(int,input().split())
q = []
for i in range(1,N+1):
    q.append(i)

new_q = []
while q:
    for i in range(K-1):
        q.append(q.pop(0))
    new_q.append(q.pop(0))

print('<', end='')
for i in range(N-1):
    print("%d, " % new_q[i], end='')
print(new_q[-1], end='')
print('>')

#######################################
from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

#########################################
# 원래 구현하고 싶었던 규칙
n, k = map(int, input().split())
q = [i for i in range(1,n+1)]
print("<",end='')
i = 0

while len(q) > 1:
    i = i+k
    if i > len(q):
        i = i % len(q)
        if i == 0 :
            i = i+ len(q)
    i = i-1
    print(q.pop(i), end=", ")

print(f'{q.pop()}>')