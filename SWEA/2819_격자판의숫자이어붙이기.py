import sys
sys.stdin=open('sample_input.txt')

T = int(input()) # 테스트케이스 수
for tc in range(1,T+1):
    board = [list(map(str,input().split())) for _ in range(4)]
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    seven = []

    for i in range(4):
        for j in range(4):
            num = [[i,j,board[i][j]]]
            while num:
                v = num.pop(0)
                if len(v[2]) == 7 :
                    seven.append(v[2])
                elif len(v[2]) < 7 :
                    for k in range(4):
                        ni = v[0] + di[k]
                        nj = v[1] + dj[k]
                        if 0 <= ni < 4 and 0 <= nj < 4: # 범위 벗어나지 않도록
                            num.append([ni,nj, v[2] + board[ni][nj]])

    seven = set(seven)
    print(f'#{tc} {len(seven)}')

########################################################################
def dfs(x,y,num):
    if len(num) == 7:
        seven.append(num)
        return
    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4 :
            dfs(ni,nj,num+board[ni][nj])

T = int(input()) # 테스트케이스 수
for tc in range(1,T+1):
    board = [list(map(str,input().split())) for _ in range(4)]
    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    seven = []

    for i in range(4):
        for j in range(4):
            dfs(i,j,'')
    seven = set(seven)
    print(f'#{tc} {len(seven)}')

##############################################
