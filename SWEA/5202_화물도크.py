import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 신청서
    time = [list(map(int,input().split())) for _ in range(N)] # 작업시작시간, 끝나는 시간 입력받기

    visited = [False] * 24
    time.sort(key=lambda x : x[1]) # 끝나는 시간 기준으로 정렬

    # 처음 작업
    cnt = 1
    for i in range(time[0][0],time[0][1]): # 처음 작업의 시작시간과 끝시간을 전부 방문
        visited[i] = True

    for i in range(1,N):
        for k in range(time[i][0],time[i][1]):
            if visited[k]:
                break
            else :
                visited[k] = True
                if k == time[i][1]-1: # 작업시간의 끝 부분까지 도달했을때만
                    cnt +=1           # 그 작업을 완료한 것으로 판단

    print(f'#{tc} {cnt}')

#############################################################
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 신청서
    time = [list(map(int, input().split())) for _ in range(N)]  # 작업시작시간, 끝나는 시간 입력받기
    time.sort(key=lambda x : x[1]) # 끝나는 시간 기준으로 정렬

    cnt = 1
    e = time.pop(0)             # 처음 일의 시작/끝 시간 꺼내기

    while time:
        if time[0][0] < e[1]:   # 일 끝나는 시간 안에 다음작업이 포함되어 있으면
            time.pop(0)         # 그 작업은 못함

        else:                   # 일 끝나는 시간 이후에 다음 작업가능한 경우
            cnt += 1            # 작업량 추가
            e = time.pop(0)     # 다음 비교를 위해 지금 시작하는 작업을 또 꺼냄

    print(f'#{tc} {cnt}')

