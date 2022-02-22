import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = [1,3]          # N 이 10일때와 20일때 초기값 설정
    # if N == 10 :
    #     print(f'#{tc} {1}')
    # elif N == 20 :
    #     print(f'#{tc} {3}')
    # else:
    #     for i in range(2, N // 10):
    #         N_list.append((N_list[i-2]*2) + N_list[i-1]) # 규칙 적용
    #     print(f'#{tc} {N_list[-1]}')
    for i in range(2, N // 10):
        N_list.append((N_list[i - 2] * 2) + N_list[i - 1])  # 규칙 적용
    print(f'#{tc} {N_list[N//10-1]}')

 # 규칙
 # N > cnt
 # 10 > 1
 # 20 > 3
 # 30 > 5   == 1*2 + 3
 # 40 > 11  == 3*2 + 5
 # 50 > 21  == 5*2 + 11
 # 60 > 43  == 11*2 + 21
 # 70 > 85  == 21*2 + 43
