import sys
input = sys.stdin.readline

def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    par[a] = b

n, m = map(int,input().split())
v = [list(map(int,input().split())) for _ in range(m)]
par = [i for i in range(n+1)]

v.sort(key=lambda x:x[2]) # 가중치 순으로 오름차순 정렬

ans = 0
for i in range(m):
    x, y = v[i][0], v[i][1]

    if find(x) == find(y):
        continue

    union_(x, y)
    ans += v[i][2]

print(ans)
