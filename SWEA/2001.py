import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    kill = [list(map(int,input().split())) for _ in range(n)] # N x N 배열

    max_val = 0
    # 앞의 두번의 for문은 MxM 배열의 개수만큼
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            # M*M 배열
            for k in range(m):
                for l in range(m):
                    cnt += kill[i+k][j+l]
            # 최대값 갱신
            if max_val < cnt :
                max_val = cnt

    print(f'#{tc} {max_val}')

