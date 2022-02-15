import sys
sys.stdin = open('sample_input.txt')

T = int(input()) #  테스트 케이스 개수

for tc in range(1,T+1):

    N = int(input()) # 칠할 영역의 개수
    purple = 0 # 보라색 칸 수
    color_map = [[0]*10 for _ in range(10)]

    for n in range(N):
        # 왼쪽 위 모서리 인덱스 r1 , c1
        # 오른쪽 아래 모서리 r2,c2
        # 색상 color
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1 : # 빨간색이면
            for i in range(r1,r2+1):
                for j in range(c1,c2+1):
                    color_map[i][j] += 1
        if color == 2 : # 파란색이면
            for i in range(r1,r2+1):
                for j in range(c1, c2+1):
                    color_map[i][j] += 1

    # 보라색 칸 수 구하기
    for i in range(10):
        for j in range(10):
            if color_map[i][j] == 2 :
                purple += 1

    print(f'#{tc} {purple}')


