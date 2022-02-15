import sys
sys.stdin = open('sample_input.txt')

T = int(input())                     # 테스트 케이스 개수

for tc in range(1,T+1):
    # 전체쪽수 P, A가 찾을 쪽 번호 Pa, B가 찾을 쪽 번호 Pb
    P , Pa, Pb = map(int,input().split())
    P_list = []
    cnt_A = cnt_B = 1

    for i in range(1,P+1):
        P_list.append(i)

    start = 0
    end = P-1
    while start <= end:
        middle = (start+end) // 2
        if P_list[middle] == Pa : # 검색성공
            break
        elif P_list[middle] > Pa :
            end = middle
        else :
            start = middle
        cnt_A += 1

    start = 0
    end = P-1
    while start <= end:
        middle = (start+end) // 2
        if P_list[middle] == Pb : # 검색성공
            break
        elif P_list[middle] > Pb :
            end = middle
        else :
            start = middle
        cnt_B += 1

    if cnt_A > cnt_B :   # cnt_B의 탐색 횟수가 더 적으므로 B 승
        print(f'#{tc} B')
    elif cnt_A < cnt_B : # cnt_A의 탐색 횟수가 더 적으므로 A 승
        print(f'#{tc} A')
    else :               # A와 B의 탐색 횟수가 같으므로 무승부
        print(f'#{tc} 0')