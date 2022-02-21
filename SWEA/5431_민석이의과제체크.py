T = int(input()) # 테스트케이스
for tc in range(1,T+1):
    n,k = map(int,input().split())
    do_work = list(map(int,input().split()))
    homework = [0] * (n+1)

    for i in do_work:
        homework[i] = 1

    print(f'#{tc}', end= ' ')
    for i in range(1,n+1):
        if homework[i] == 0 :
            print(i, end=' ')
    print()