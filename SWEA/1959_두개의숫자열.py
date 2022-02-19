T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))

    total = 0
    if n < m :
        for i in range(m-n+1):
            abSum = 0
            for j in range(n):
                abSum += Ai[j] * Bj[i+j]

            if abSum > total:
                total = abSum

    else :
        for i in range(n-m+1):
            abSum = 0
            for j in range(m):
                abSum += Ai[i+j] * Bj[j]

            if abSum > total:
                total = abSum

    print(f'#{tc} {total}')