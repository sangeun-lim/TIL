import sys
sys.stdin=open('sample_input.txt')

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[False]*N for _ in range(N)]
#
#     min_total = 99999999
#     sub_total = 0
#
#     while
#         visited = [[False] * N for _ in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 if i == j :
#                     visited[i][j] = True
#                 else :
#                     if not visited[i][j]:
#                         sub_total += arr[i][j]
#                         # 행 전체 True로, 열 전체 True로 만들기
#                         visited[i][j] = True
#
#     print(min_total)

##################################################################

# idx는 배터리 사용횟수(?) , y = 열, ssum 은 합
# idx,y ===> 0,1 ==> 1,2 == > 2,0 or 0,2 ==> 2,1 ==> 1,0 형태

def DFS(idx, y, ssum):
    global min_total

    if min_total < ssum : # 가지치기
        return

    # 종료조건
    if idx == N-1: # 마지막 차례이면
        ssum += arr[y][0] # 돌아와야 하는 사무실의 소비량 더해주고
        if min_total > ssum:
            min_total = ssum # 최소값 갱신
            return

    for i in range(1,N): # 마지막으로 방문할 사무실 제외하고 관리구역 돌기 , 0열 값 제외
        # arr 배열에서 값이 0 이면 넘어가기
        if arr[y][i] == 0:
            continue
        # 아직 방문하지 않았다면
        if not visited[i] :
            visited[i] = True
            DFS(idx+1, i, ssum + arr[y][i])
            visited[i] = False


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False]*N
    min_total = 99999999
    DFS(0,0,0)
    print(f'#{tc} {min_total}')