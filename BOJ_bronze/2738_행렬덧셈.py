n, m = map(int,input().split())
lst1 = [list(map(int,input().split())) for _ in range(n)]
lst2 = [list(map(int,input().split())) for _ in range(n)]
lst3 = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        lst3[i][j] = lst1[i][j] + lst2[i][j]

for i in range(n):
    for j in range(m):
        print(lst3[i][j], end=' ')
    print()