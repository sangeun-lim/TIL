import sys
sys.stdin=open('input.txt')

def dfs(start,end):
    stack = [start]                         # stack 초기화
    visited = [False] * (100)               # 방문 여부를 검사
    while stack :                           # stack이 빌때까지
        v = stack.pop()                     # 시작 정점을 stack에서 꺼내고 다른 변수에 저장
        visited[v] = True                   # 방문했다는 것을 표시
        for w in range(100):                # 연결된 정점들 찾기
            if visited[w] == 0 :            # 방문하지 않았다면
                if G[v][w] == 1:            # 간선이 있다면 == 연결되어있다면
                    stack.append(w)         # 갈 수 있는 곳이므로 stack에 추가
    return visited[end]                     # True 면 start부터 end 까지의 경로가 있는 것

for tc in range(1,11):                      # 총 10개의 테스트 케이스
    T,N = map(int,input().split())          # T =  테스트 케이스 번호, N = 길의 총 개수
    G = [[0]*100 for _ in range(100)]       # 정점의 개수가 최대 100개이기도 하고, 확인해야할 끝점이 인덱스 99이므로 100x100 배열 생성
    temp = list(map(int,input().split()))   # 연결된 정점 정보 입력 받기

    for i in range(N):
        G[temp[i*2]][temp[i*2+1]] = 1       # 방향성이 있으므로, temp의 0,2,4... 인덱스를 출발지점으로, 1,3,5...를 연결지점으로

    # 출력 조건에 맞게 출력
    if dfs(0,99):
        print(f'#{T} {1}')
    else:
        print(f'#{T} {0}')
