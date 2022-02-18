import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스 개수

for tc in range(1,T+1):
    # NxN 글자판
    # 길이가 M 인 회문
    N, M = map(int,input().split())
    board = [input() for _ in range(N)]

    #출력에 쓰일 리스트
    ans = []

    # 가로
    for i in range(N):
        for j in range(N - M + 1):
            if board[i][j:j+M] == board[i][j:j+M][::-1]:  # 회문 확인
                ans.append(board[i][j:j+M])               # 결과 리스트에 추가

    # 세로
    # 이해하는중입니다 ^__^
    for i in range(N - M + 1):
        for j in range(N):
            col_list = []
            for k in range(M):
                col_list.append(board[k+i][j])
            if col_list == col_list[::-1]:
                ans.append(''.join(col_list))

    print(f'#{tc} {ans[0]}')