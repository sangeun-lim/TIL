for tc in range(3):
    n = input()
    max_V = 0

    cnt = 1

    for i in range(1,len(n)):
        if n[i-1] == n[i]:
            cnt += 1
        else :
            cnt = 1
        if max_V < cnt:
            max_V = cnt

    print(max_V)
