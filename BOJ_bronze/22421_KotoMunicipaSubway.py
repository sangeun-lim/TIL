while True:
    D , E = map(int,input().split())
    min_ = 99999999
    if D == 0 and E == 0:
        exit()
    for i in range(D+1):
        min_ = min(min_, abs((i**2 + (D-i)**2)**0.5-E))

    print(min_)
