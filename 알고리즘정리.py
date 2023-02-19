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

# 다이나믹 프로그래밍


































