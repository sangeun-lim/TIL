import sys
sys.stdin = open('sample_input.txt')

T = int(input())                          # 테스트 케이스 수

# for i in  range(1,T+1):
#     N = int(input())                      # 입력받을 수의 개수
#     num = list(map(int,input().split()))  # 입력 받을 수들을 리스트에 저장
#
#     maxValue = 0                          # 최대값 초기화
#     minValue = 1000001                    # 최소값 초기화
#
#     for j in range(N):
#         if maxValue < num[j]:             # 리스트 내 최대값 갱신
#             maxValue = num[j]
#
#         if minValue > num[j]:             # 리스트 내 최소값 갱신
#             minValue = num[j]
#
#     min_max = maxValue - minValue         # 최대값-최소값
#
#     print(f'#{i} {min_max}')

def bubble_sort(arr):
    for i in range(len(arr)-1, 0,-1):
        for j in range(i):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1], arr[j]

for i in  range(1,T+1):
    N = int(input())                      # 입력받을 수의 개수
    num = list(map(int,input().split()))  # 입력 받을 수들을 리스트에 저장
    bubble_sort(num)

    print(f'#{i} {num[-1] - num[0]}')