import sys
sys.stdin = open('sample_input.txt')

T = int(input())                              # 노선 수

for tc in range(1, T+1):
    k, n, m = map(int, input().split())       # 최대 이동 정류장 수 k, 종점 n, 충전기 설치개수 m
    m_list = list(map(int, input().split()))  # 충전기가 설치된 정류장 위치
    bus = [0 for i in range(n+1)]

    for i in m_list:
        bus[i] = 1

    point = 0                                   # 현재 위치
    cnt = 0                                     # 충전횟수

    for j in range(m):
        point += k                              # 현재위치 + 버스의 이동 정류장 수
        if point >= n :                         # 종점을 지나면
            break                               # 조건문 종료

        for l in range(point, point-k, -1):     # 충전할 수 있는 마지노선 정류장에서 뒤로 한칸씩
            if bus[l]:                          # 충전소가 있다면
                cnt += 1                        # 충전횟수 증가
                point = l                       # 버스 위치 갱신
                break
        else :                                  # 충전기 설치가 잘못되었다면
            cnt = 0
            break
    print(f'#{tc} {cnt}')