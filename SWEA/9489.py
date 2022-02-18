import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    NM = [list(map(int,input().split())) for _ in range(N)]

    longest = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 오른쪽으로 1 일때
            if NM[i][j] == 1:
                cnt += 1
                if longest < cnt:
                    longest = cnt
            else :
                cnt = 0

    for j in range(M):
        for i in range(N):
            # 아래쪽으로 1 일때
            if NM[i][j] == 1:
                cnt += 1
                if longest < cnt:
                    longest = cnt
            else:
                cnt = 0

    print(f'#{tc} {longest}')
