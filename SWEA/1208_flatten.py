import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    dump_times = int(input())
    boxes = list(map(int,input().split()))

    heights = [0] * 101                     # 박스 높이의 분포를 카운팅하기 위한 초기화
    max_height = 0
    min_height = 100

    for box in boxes:
        heights[box] += 1
        if max_height < box :
            max_height = box
        if min_height > box :
            min_height = box

    for dump in range(dump_times):
        if max_height - min_height < 2:
            break
        heights[max_height] -= 1
        heights[max_height-1] += 1
        heights[min_height] -= 1
        heights[min_height+1] += 1

        if heights[max_height] == 0 :
            max_height -= 1
        if heights[min_height] == 0 :
            min_height += 1

    result = max_height - min_height # 최대 높이와 최소 높이의 차이
        
    print(f'#{tc} {result}')
