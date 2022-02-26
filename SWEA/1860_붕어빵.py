import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())        # N : 사람수, M : M초, K: M초동안 K개
    come = list(map(int,input().split()))   # 몇 초에 도착하는지 N명만큼 받음
    come.sort()                             # 오는 순서 정렬
    result = 1                              # 성공 여부 판단할 변수

    # 사람이 언제 오냐를 주어진 x초까지 총 붕어빵이 몇개 만들어지는 느낌으로 생각(?)
    for i in range(N): # x초까지 만들어지는 붕어빵의 개수는 (x // M) * K
        bread = (come[i] // M) * K - (i+1) # 1인당 1개씩 구매
        if bread < 0:
            result = 0
            break

    if result == 1 :
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')


# def bread_count(N, M, K, tc):
#     cycle_time = list(map(int, input().split()))
#     cycle_time = sorted(cycle_time, reverse=True)
#     bread_cnt = 0  # 남은 빵 개수
#     time = 0  # 현재 시간
#     cnt = 0  # 온 사람 카운트
#
#     while cnt != N:
#         # work 시간이 되면 뿡어빵 생성
#         time += M
#         bread_cnt += K
#         # 손님이 오면 빵이 줄어든다
#         for i in range(N):
#             if cycle_time[i] < M:
#                 return 'Impossible'
#             if time <= cycle_time[i] < time + M:
#                 bread_cnt -= 1
#                 cnt += 1
#         if bread_cnt < 0:
#             return 'Impossible'
#
#     return 'Possible'