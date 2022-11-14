N = int(input())
for i in range(N):
    M = int(input())
    x = []
    y = []
    z = []
    total = 0
    for j in range(M):
        x1, y1 ,z1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
        z.append(z1)
    k,d,a = map(int,input().split())
    for j in range(M):
        kda_sum = x[j] * k - (y[j] * d) + z[j] * a
        total += max(0,kda_sum)
    print(total)

#################################
for _ in range(int(input())):
    l = []
    for i in range(int(input())):
        l.append(list(map(int,input().split())))
    a,b,c = map(int,input().split())
    s = 0
    for i in l:
        s += max(0,i[0]*a + i[2]*c - i[1]*b)
    print(s)