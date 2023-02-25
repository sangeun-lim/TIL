# DFS 소스코드 (스택 자료구조 or 재귀함수 이용)
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고
#    방문 처리함. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복함

def dfs(graph, v, visitied):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visitied[i]:
            dfs(graph, i, visitied)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

dfs(graph, 1, visited)