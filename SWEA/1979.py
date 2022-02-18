import sys
sys.stdin= open('input.txt')

T = int(input()) # 테스트 케이스

for tc in range(1,T+1):
    n , k = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(n)]

    possible = 0

    # 행방향이 K 일때 cnt 구하기
    for i in range(n):
        cnt = 0
        for j in range(n):
            # 위치값이 1이면 넣을 수 있는 단어 수 증가
            if puzzle[i][j]:
                cnt += 1
            # 위치값이 0 일 때
            else :
                # 넣을 수 있는 단어값이 k 와 같다면
                if cnt == k :
                    possible += 1 # k길이 단어를 넣을 수 있는 횟수 증가
                cnt = 0
        # 행의 끝이 1로 끝났을 때 넣을 수 있는 단어값이 k 와 같다면
        if cnt == k:
            possible += 1         # k길이 단어를 넣을 수 있는 횟수 증가

    # 열방향이 K 일때 cnt 구하기
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == k :
                    possible += 1
                cnt = 0
        if cnt == k:
            possible += 1

    print(f'#{tc} {possible}')