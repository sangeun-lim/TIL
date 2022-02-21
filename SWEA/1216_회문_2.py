import sys
sys.stdin = open('input.txt')

# 행기준 계산
def palindrome(arr):
    max_V = 0                                   # return 할 가장 큰 회문의 길이
    for i in range(100,0,-1):
        if max_V >= i :                         # 100부터 점점 작아지므로 처음 회문 나온 값이 가장 큰 값이 되고 반복문 종료
            break
        for j in range(100):                    # 총 100줄 이니까 100번 반복
            for k in range(100-i+1):
                if arr[j][k:k+i] == arr[j][k:k+i][::-1]: # 회문인지 확인
                    V = len(arr[j][k:k+i])      # 회문 길이 저장
                    if V > max_V :              # 회문 길이 갱신
                        max_V = V
    return max_V

for tc in range(10):
    n = input()
    board = [input()for _ in range(100)]       # 100 x 100 배열 입력 받기

    max_V1 = palindrome(board)                 # 행 기준 가장 긴 회문의 길이 구하기
    board2 = list(map(list, zip(*board)))      # 전치 행렬로 변환
    max_V2 = palindrome(board2)                # 열 기준 가장 긴 회문의 길이 구하기

    real_max = 0                               # 출력할 최종 회문의 길이

    # 크기 비교
    if max_V1 > max_V2 :
        real_max = max_V1
    else :
        real_max = max_V2

    print(f'#{tc + 1} {real_max}')

    # 행 부분 계산
    # for i in range(100,0,-1):
    #     if max_V >= i :
    #         break
    #     for j in range(100):
    #         for k in range(100-i+1):
    #             if board[j][k:k+i] == board[j][k:k+i][::-1]:
    #                 V = len(board[j][k:k+i])
    #                 if V > max_V :
    #                     max_V = V
    #
    # # 열 부분 계산
    # for i in range(100,0,-1):
    #     if max_V >= i :
    #         break
    #     for j in range(100-i+1):
    #         for k in range(100):
    #             col_list = []
    #             for l in range(i):
    #                 col_list.append(board[l+j][k])
    #             if col_list == col_list[::-1]:
    #                 V = len(col_list)
    #             if V > max_V:
    #                 max_V = V
    # print(f'#{tc + 1} {real_max}')


def check(a):                   #a: list
    l = len(a)
    for i in range(l // 2):
        if a[i] != a[l - i - 1]:
            return False
    return True

for _ in range(10):
    tc = input()
    map_list = [list(map(str, input())) for _ in range(100)]
    map_list2 = [[0]*100 for _ in range(100)]               #map_list2: map_list전치
    length = 100                                            #회문 길이

    for i in range(100):
        for j in range(100):
            map_list2[i][j] = map_list[j][i]

    # for i in range(N):
    #     map_list.append(input())
    # for i in range(N):
    #     str_temp = ''
    #     for k in range(N):
    #         str_temp += map_list[k][i]
    #     map_list2.append(str_temp)
    result = 0                          #최종 회문의 길이_초깃값
    for H in range(length, 0, -1):      #H: 회문길이 변화
        if result >= H:                 #아래 반복문에서 result가 결정된 경우, 종료 위함
            break
        for i in range(100):            #행 고정
            if result == H:             #아래 for 반복하면서 결정된 최종 회문의 길이
                break
            for j in range(100 - H + 1):    #정해둔 H의 길이에 맞는 회문 찾기
                if check(map_list[i][j:j + H]) or check(map_list2[i][j:j + H]):
                    result = H              #회문이 확인되었다면 그때의 H가 회문의 길이
                    break

    print(f'#{tc} {result}')