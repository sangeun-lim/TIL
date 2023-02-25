# 재귀 함수
# 반복으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성
    return n * factorial_recursive(n - 1)
print(factorial_iterative(5))
print(factorial_recursive(5))

#--------------------------------------------------------------------#

#최대공약수 계산(유클리드 호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
print(gcd(192,162))

#--------------------------------------------------------------------#

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

#--------------------------------------------------------------------#

# BFS 소스코드 (큐 자료구조 이용)
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
#    모든 큐에 삽입하고 방문 처리함.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복함.

from collections import deque
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue  = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

bfs(graph, 1, visited)

#--------------------------------------------------------------------#

# 선택 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

#--------------------------------------------------------------------#

# 삽입 정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0 , -1): # 인덱스  i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

#--------------------------------------------------------------------#

# 퀵 정렬 소스코드 1
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

#--------------------------------------------------------------------#

# 퀵 정렬 소스코드 2
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#--------------------------------------------------------------------#

# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

#--------------------------------------------------------------------#

# 이진 탐색 소스코드 (재귀함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

#--------------------------------------------------------------------#

# 이진 탐색 소스코드 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else :
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

#--------------------------------------------------------------------#

# 파이썬 이진 탐색 라이브러리
# from bisect import bisect_left, bisect_right
# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

#--------------------------------------------------------------------#

# 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a,left_value)
    return right_index - left_index

# 배열 선언
a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1,3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

#--------------------------------------------------------------------#

# 다이나믹 프로그래밍(동적 계획법)
# 1. 최적부분구조
#    큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제 해결
# 2. 중복되는 부분 문제
#    동일한 작은 문제를 반복적으로 해결
# 탑다운(하향식) 방식(메모이제이션)

# 피보나치 수열: 탑다운 다이나믹 프로그래밍
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
dp = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]
print(fibo(99))

#--------------------------------------------------------------------#

# 피보나치 수열: 바텀업 다이나믹 프로그래밍

dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

#반복문으로 구현
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

#--------------------------------------------------------------------#

# n x m 형태가 1차원 리스트로 주어졌을 때
# 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
n,m = map(int,input().split())
array = list(map(int,input().split()))
dp = []
index = 0
for i in range(n):
    dp.append(array[index:index + m])
    index += m

#--------------------------------------------------------------------#

# LIS 알고리즘(가장 긴 증가하는 부분 수열)
n = int(input())
arr = list(map(int,input().split()))
dp = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

#--------------------------------------------------------------------#

# 다익스트라 최단경로 알고리즘
# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 5. 3번과 4번 반복

# 다익스트라 알고리즘 간단 구현
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

#--------------------------------------------------------------------#

# 우선순위 큐 - Heap
# 최소힙
import heapq

# 오름차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value) # 특정 리스트에 데이터 넣는 heappush
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#--------------------------------------------------------------------#
# 최대힙
import heapq

# 내림차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

#--------------------------------------------------------------------#

# 다익스트라 알고리즘: 개선된 구현 방법 (힙 자료구조 사용)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstart(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print('INFINITY')
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

#--------------------------------------------------------------------#

# 플로이드 워셜 알고리즘
# 모든 노드에서 다른 모든 노드까지의 최단 경로를 모두 계산

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트를 만들고, 무한으로 초기화
graph =[[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한으로 출력
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=' ')
    print()

#--------------------------------------------------------------------#

# 서로소 집합: 공통 원소가 없는 두 집합
# 합치기 찾기(Union Find) 자료구조
# 서로소 집합 자료구조: 기본적인 구현 방법

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int,input().split())
parent = [0] * (v+1)# 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int,input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

#--------------------------------------------------------------------#

# 서로소 집합 자료구조: 경로 압축
# 찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#--------------------------------------------------------------------#

# 서로소 집합을 활용한 사이클 판별
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
    # 1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산 수행
    # 2) 루트 노드가 서로 같다면 사이클이 발생한것
# 2. 모든 간선에 대하여 1번 과정 반복

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생함')
else:
    print('사이클이 발생하지 않음')

#--------------------------------------------------------------------#

# 신장 트리: 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘 : 최소 신장 트리 알고리즘
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    # 1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
    # 2) 사이클이 발생한 경우 최소 신장 트리에 포함 X
# 3. 2번 과정 반복

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int,input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합을 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

#--------------------------------------------------------------------#

# 위상 정렬 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열
# DAG 에서만 수행 가능(순환하지 않는 방향 그래프)
# 큐를 이용하여 구현
# 1. 진입차수가 0인 모든 노드를 큐에 넣음
# 2. 큐가 빌 때까지 다음의 과정을 반복
    # 1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
    # 2) 새롭게 진입차수가 0이 된 노드를 큐에 넣음
# 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 동일

# DFS로도 구현 가능하지만 다루지 않음

from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
v, e = map(int,input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b) # 정점 A에서 B로 이동가능
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

#--------------------------------------------------------------------#

# 소수 판별 알고리즘 : 기본
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2,x):
        # x 가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

#--------------------------------------------------------------------#

# 소수 판별 알고리즘 : 개선
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0 :
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

#--------------------------------------------------------------------#

# 다수의 소수 판별
# 에라토스테네스의 체
# 1. 2부터 N까지 모든 자연수 나열
# 2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i를 찾음
# 3. 남은 수 중에서 i의 배수를 모두 제거 (i는 제거하지 않음)
# 4. 2번과 3번 반복

import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인것으로 초기화(0과 1은 제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘 수행
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

#--------------------------------------------------------------------#

# 투 포인터 (ex문제: 특정한 합을 가지는 부분 연속 수열 찾기)
n = 5 # 데이터의 개수
m = 5 # 찾고자 하는 부분합
data = [1,2,3,2,5] # 전체수열

cnt = 0
interval_sum = 0
end = 0

for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[start]

print(cnt)

#--------------------------------------------------------------------#

# 구간 합(접두사 합(prefix sum) 이용하기)
n = 5
data = [10,20,30,40,50]

# 접두사 합(prefix sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])

#--------------------------------------------------------------------#

# 트리의 순회

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        pre_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
    print(node.data, end=' ')

n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

#--------------------------------------------------------------------#

# 벨만 포드 최단 경로 알고리즘
# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 다음 과정 N-1번 반복
#     1) 전체 간선 E개를 하나씩 확인
#     2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 4. 음수 간선 순환이 발생하는지 체크하고 싶다면 3번과정 한번 더 수행
# - 이때 테이블이 갱신된다면 음수 간선 순환 존재

import sys
input = sys.stdin.readline
INf = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int,input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우, -1을 출력
        if dist[i] == INF:
            print('-1')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(dist[i])

#--------------------------------------------------------------------#

# 바이너리 인덱스 트리(펜윅 트리)

import sys
input = sys.stdin.readline

# 데이터의 개수, 변경 횟수, 구간 합 계산 횟수
n, m, k = map(int,input().split())

# 전체 데이터의 개수는 최대 1000000개
arr = [0] * (n+1)
tree = [0] * (n+1)

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0이 아닌 마지막 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result

# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

# start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)

for i in range(m+k):
    a,b,c = map(int,input().split())
    # 업데이트 연산인 경우
    if a == 1:
        update(b, c - arr[b]) # 바뀐 크기(dif)만큼 적용
        arr[b] = c
    # 구간 합 연산인 경우
    else:
        print(interval_sum(b, c))

#--------------------------------------------------------------------#

# 최소 공통 조상(LCA)
# 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제
# 1. 모든 노드에 대한 깊이를 계산
# 2. 최소 공통 조상을 찾을 두 노드를 확인
#     1) 먼저 두 노드의 깊이가 동일하도록 거슬러 올라감
#     2) 이후 부모가 같아질 떄까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
# 3. 모든 LCA(a,b) 연산에 대하여 2번의 과정 반복

import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # 먼저 깊이가 동일하도록
while d[a] != d[b]:
    if d[a] > d[b]:
        a = parent[a]
    else:
        b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))

#--------------------------------------------------------------------#

# 최소 공통 조상(LCA) 개선

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5)) # 런타임 오류 피하기
LOG = 21 # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1,0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이가 동일하도록
    for i in range(LOG -1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG -1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())
for i in range(m):
    a, b = map(int,input().split())
    print(lca(a,b))
