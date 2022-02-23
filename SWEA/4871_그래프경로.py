import sys
sys.stdin=open('sample_input.txt')
# from pprint import pprint

def dfs(start,end):
    stack = [start]                     # stack 초기화
    visited = [False] * (V+1)           # 방문 여부를 검사
    while stack :                       # stack이 빌때까지
        v = stack.pop()                 # 시작 정점을 stack에서 꺼내고 다른 변수에 저장
        visited[v] = True               # 방문했다는 것을 표시
        for w in range(V+1):
            if visited[w] == 0 :        # 방문하지 않았다면
                if G[v][w] == 1:        # 간선이 있다면
                    stack.append(w)     # 연결되어 있으므로 stack에 추가
    # print(visited)
    return visited[end]                 # True 면 경로가 있는 것

T = int(input())                        # 테스트 케이스 수
for tc in range(1,T+1):
    V,E = map(int,input().split())              # V = 노드 수 , E = 간선 수
    G = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):                          # G에 연결된 정점 표시해주기
        s,e = map(int,input().split())
        G[s][e] = 1
    # pprint(G)
    S,g = map(int,input().split())              # 확인할 시작 노드 와 끝 노드 입력 받기
    if dfs(S,g):
        print(f'#{tc} {1}')
    else :
        print(f'#{tc} {0}')