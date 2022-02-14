import sys
sys.stdin = open('input.txt')

T = 10

for i in range(T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    arr_len = len(arr)
    max_arr = []             # 각 행의 합, 각 열의 합, 각 대각선의 합 저장

    for j in range(arr_len):
        arr_sum = 0
        arr_sum2 = 0
        for k in range(arr_len):
            arr_sum += arr[j][k]    # 각 행의 합
            arr_sum2 += arr[k][j]   # 각 열의 합
        max_arr.append(arr_sum)
        max_arr.append(arr_sum2)

    arr_sum3 = 0
    arr_sum4 = 0
    for j in range(arr_len):
        for k in range(arr_len):
            if j == k:
                arr_sum += arr[j][k]   # 각 대각선의 합
            if j + k == 99:
                arr_sum += arr[j][k]   # 각 엇대각선의 합

        max_arr.append(arr_sum3)
        max_arr.append(arr_sum4)


    print(f'#{N} {max(max_arr)}')


