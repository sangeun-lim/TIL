'''
union find 최적화 두가지

1. 경로 압축 << find를 최적화 << logN 의 시간복잡도
2. union by rank << union을 최적화
둘다 하면 상수의 시간복잡도
'''
import sys
input = sys.stdin.readline

def find(x): # 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

    # if par[x] != x:
    #     par[x] = find(par[x])  # 경로 압축
    # return par[x]

def union(a, b): # 같은 루트를 가지게함, 합집합
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] < rank[b]:
        par[a] = b
    elif rank[a] > rank[b]:
        par[b] = a
    else:
        par[a] = b
        rank[b] += 1

n, m = map(int,input().split())
par = [i for i in range(1000010)]
rank = [0 for i in range(1000010)]

for i in range(m):
    a, b, c = map(int,input().split())

    if a == 0:
        union(b,c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")