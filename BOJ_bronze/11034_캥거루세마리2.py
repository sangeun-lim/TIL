while True:
    try:
        A,B,C = map(int,input().split())
        if B-A <= C-B:
            print(C-B-1)
        else:
            print(B-A-1)
    except:
        break