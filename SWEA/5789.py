T = int(input()) # Test Case 개수

for tc in range(1,T+1):
    N, Q = map(int,input().split()) # 테스트 케이스
    box = [0 for _ in range(N)]

    for i in range(1,Q+1):
        l, r = map(int,input().split())
        for j in range(l-1,r):
            box[j] = i

    print(f'#{tc}', end=' ')
    print(' '.join(map(str, box)))
    ###################################
    print(f'#{tc}', *box)