T = int(input()) # 테스트 케이스 개수

for tc in range(1,T+1):
    N = int(input())  # 다니는 버스의 수
    bus_stop = [0] * 5001

    for i in range(N):
        A,B = map(int,input().split())
        # A~B를 지나는 버스 노선 누적
        for j in range(A,B+1):
            bus_stop[j] += 1

    P = int(input()) # 확인할 버스 정류장 수

    print(f'#{tc}', end = ' ')
    for i in range(P):
        C = int(input())  # 확인하고 싶은 정류장 번호
        print(bus_stop[C], end=' ')
    print()

##########################################################
T = int(input()) # 테스트 케이스 개수

for tc in range(1,T+1):
    N = int(input())  # 다니는 버스의 수
    AB = [list(map(int,input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]
    bus_stop = [0] * P

    for i in range(N):
        for j in range(P):
            if AB[i][0] <= C[j] <= AB[i][1]:
                bus_stop[j] += 1
    print(f'#{tc}', *bus_stop)