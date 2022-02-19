import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    sdoqu = [list(map(int,input().split())) for _ in range(9)]

    number = [1,2,3,4,5,6,7,8,9]
    cnt = 0

    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(sdoqu[i][j])
            col.append(sdoqu[j][i])
        row.sort()
        col.sort()
        if row == number and col == number:
            cnt += 2
        # if col == number:
        #     cnt += 1

    for i in range(0,9,3):
        for j in range(0,9,3):
            square = []
            for k in range(3):
                for l in range(3):
                    square.append(sdoqu[i+k][j+l])
            square.sort()
            if square == number:
                cnt += 1
    if cnt == 27:
        print(f'#{tc} 1')
    else :
        print(f'#{tc} 0')

