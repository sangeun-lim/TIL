import sys
sys.stdin = open('sample_input.txt')

T = int(input())                     # 테스트 케이스 개수

for tc in range(1,T+1):
    N = int(input())                        # 입력되는 정수의 개수
    num = list(map(int,input().split()))    # 입력된 정수의 리스트

    # 들어온 리스트 정렬 (오름차순)
    # 버블 정렬
    for i in range(N-1):
        for j in range(N-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    sort_list = [0] * N                          # 특별하게 정렬된 값을 저장할 리스트

    for i in range(N):
        # 짝수번째 인덱스는 큰 순서로 0 2 4 6 8
        # 새로운 리스트[0] = num[9]  # N - 1  = 9
        # 새로운 리스트[2] = num[8]  # N - 2  = 8
        # 새로운 리스트[4] = num[7]  # N - 3  = 7
        # 새로운 리스트[6] = num[6]  # N - 4  = 6
        # 새로운 리스트[8] = num[5]  # N - 5  = 5
        if i % 2 == 0:
            sort_list[i] = num[N - (i // 2) - 1]
        # 홀수번째 인덱스는 작은 순서로 1 3 5 7 9
        # 새로운 리스트[1] = num[0]  # i - 1  = 0
        # 새로운 리스트[3] = num[1]  # i - 2  = 1
        # 새로운 리스트[5] = num[2]  # i - 3  = 2
        # 새로운 리스트[7] = num[3]  # i - 4  = 3
        # 새로운 리스트[9] = num[4]  # i - 5  = 4
        else:
            sort_list[i] = num[i - (i + 1) // 2]

    #10개까지만 출력
    print(f'#{tc}', end=' ')
    for i in range(10):
        print(sort_list[i], end=' ')
    print()
    #################
    # print(*sort_list[:10])