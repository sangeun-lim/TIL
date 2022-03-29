import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    w = list(map(int,input().split())) # N개의 화물의 무게
    t = list(map(int,input().split())) # M 개의 트럭의 적재용량

    # 화물의 무게와 트럭의 적재용량을 큰 순서대로 정렬
    w.sort(reverse=True)
    t.sort(reverse=True)

    move = 0 # 트럭들의 최대 적재 용량의 합

    while w and t: # 트럭이 다 담기거나, 화물을 다 담지 못하거나
        if t[0] >= w[0]:
            move += w.pop(0)
            t.pop(0)

        else :
            w.pop(0)

    print(f'#{tc} {move}')