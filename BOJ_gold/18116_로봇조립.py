import sys
input = sys.stdin.readline

par = [i for i in range(1000010)]
rank = [0 for i in range(1000010)]
sz = [1 for i in range(1000010)]

def find(x): # 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(a, b): # 같은 루트를 가지게함, 합집합
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] < rank[b]:
        par[a] = b
        sz[b] += sz[a]
    elif rank[a] > rank[b]:
        par[b] = a
        sz[a] += sz[b]
    else:
        par[a] = b
        sz[b] += sz[a]
        rank[b] += 1

n = int(input())
for i in range(n):
    a, *b = input().split()
    if a == 'I':
        union(int(b[0]), int(b[1]))
    else:
        print(sz[find(int(b[0]))])