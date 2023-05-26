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
v = [list(map(int,input().split())) for i in range(m)]
s, e = map(int,input().split())
par = [i for i in range(n+1)]

v.sort(key=lambda x:-x[2]) # 중량제한 기준으로 내림차순 정렬

for i in range(m):
    union_(v[i][0], v[i][1])

    if find(s) == find(e):
        print(v[i][2])
        break