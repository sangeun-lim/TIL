T = int(input())

for tc in range(1,T+1):
    N = int(input())
    C = list(map(int,input().split()))

    cnt = 1
    max_value = 1

    for i in range(N-1):
        if C[i] < C[i+1]:
            cnt += 1
            if max_value < cnt :
                max_value = cnt
        else :
            cnt = 1

    print(f'#{tc} {max_value}')