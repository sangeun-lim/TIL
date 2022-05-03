while True :
    N, M = map(int, input().split())
    if N == M == 0:
        break
    total = 0
    NM = M / N
    arr = list(map(int, input().split()))
    for i in arr:
        if i >= NM:
            total += NM
        else :
            total += i
    print(int(total))