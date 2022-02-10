import sys
sys.stdin = open('sample_input.txt')

T = int(input())                          # 테스트 케이스 수

for i in range(1, T+1):
    n, m = map(int, input().split())      # 정수 n 개와 구간 개수 m
    num = list(map(int,input().split()))  # 입력 받을 수들을 리스트에 저장

    max_m = 0
    min_m = 99999999

    for j in range(n-m+1):
        num_sum = 0            # M개의 합을 저장할 변수
        for k in range(j,j+m):     # 구간 개수만큼 반복
            num_sum += num[k]

        if max_m < num_sum :   # 최대값 갱신
            max_m = num_sum

        if min_m > num_sum :   # 최소값 갱신
            min_m = num_sum

    min_max = max_m - min_m  # 최대값-최소값

    print(f'#{i} {min_max}')

    # lst = []
    # for i in range(n-m+1):
    #     lst.append(sum(num[i:i+m]))
    #
    # print('#%s %d'%(tc, max(lst)-min(lst)))
