import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    start_list = []        # 시작점을 담아줄 리스트

    # 0행에서 시작점들 모두 찾아주기
    for i in range(0,100):
        if ladder[0][i] == 1 :
            start_list.append(i-1)

    # end = 0 # 출발지점 저장해줄 변수

    for start in start_list:
        x = start
        y = 0

        while y < 99:
            # 오른쪽이 1 이면 오른쪽으로
            if ladder[y][x+1]:
                # 오른쪽 벽까지
                while ladder[y][x+1]:
                    x += 1
                else :
                    y += 1

            # 왼쪽이 1이면 왼쪽으로
            elif ladder[y][x-1]:
                # 왼쪽 벽까지
                while ladder[y][x-1] :
                    x -= 1
                else :
                    y += 1

            # 왼쪽, 오른쪽 둘다 0 이면 아래쪽으로
            else :
                y += 1
        if ladder[y][x] == 2 :
            print(f'#{tc} {start}')


