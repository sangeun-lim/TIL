T = int(input())

for tc in range(1,T+1):
    cnt = [0] * 1001 # 1~1000
    N = int(input())    # 노선수
    bus = [list(map(int,input().split())) for _ in range(N)] # bus[i][0] = 버스타입 , bus[i][1] = 출발정류장 번호 A, bus[i][2] = 종점 정류장 번호 B

    for i in range(N):
        if bus[i][0] == 1 : # 일반버스인경우
            for j in range(bus[i][1], bus[i][2]+1): # 모든 정류장 정차
                cnt[j] += 1
        elif bus[i][0] == 2: # 급행 버스인 경우
            for j in range(bus[i][1], bus[i][2] , 2):
                cnt[j] += 1
            cnt[bus[i][2]] += 1
        else : # 광역 급행 버스인 경우
            cnt[bus[i][1]] += 1
            cnt[bus[i][2]] += 1
            if bus[i][1] % 2 == 0: # A가 짝수인 경우 A~B 사이의 모든 4의 배수 정류장 정차
                for j in range(bus[i][1]+1,bus[i][2]):
                    if j % 4 == 0 :
                        cnt[j] += 1
            else : # A가 홀수인 경우 A~B사이의 모든 3의 배수이면서 10의 배수가 아닌 정류장 정차
                for j in range(bus[i][1]+1,bus[i][2]):
                    if j % 3 == 0 and j % 10 != 0:
                       cnt[j] += 1

    print(f'#{tc} {max(cnt)}')

####################
# T = int(input())
#
# for tc in range(1,T+1):
#     cnt = [0] * 1001                                # 1~1000
#     N = int(input())                                # 노선수
#     for _ in range(N):                              # 노선수만큼 반복
#         K,A,B = map(int,input().split())
#         if K == 1:                                  # 일반 버스, 모든 정류장 정차
#             for i in range(A,B+1):
#                 cnt[i] += 1
#         elif K == 2 :                               # 급행버스 , A가 짝수면 짝수만, 홀수면 홀수만, B에도 정차
#             for i in range(A,B,2):
#                 cnt[i] += 1
#             cnt[B] += 1
#         else :                                       # 광역버스 , 별도 처리
#             cnt[A] += 1
#             cnt[B] += 1
#             for i in range(A+1, B):
#                 if A % 2 == 0 and i % 4 == 0 :
#                     cnt[i] += 1
#                 elif A % 2 == 1 and i % 3 == 0 and i % 10 != 0 :
#                     cnt[i] += 1
#     maxV = 0
#     for i in range(1,1001):
#         if cnt[i] == 3:
#             maxV += 1
#     print(f'#{tc} {maxV}')
