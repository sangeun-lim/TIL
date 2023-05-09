N, M = map(int,input().split())
lst = [0] * N
for _ in range(M):
    i, j, k = map(int,input().split())
    for ball in range(i-1,j):
        lst[ball] = k
print(*lst)