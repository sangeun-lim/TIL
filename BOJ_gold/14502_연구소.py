n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [-1,1,0,0]
cnt = 0

def bfs():
    global cnt
    arr2 = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr2[i][j] = arr[i][j]
    result = 0
    new_arr = []
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 2 :
                new_arr.append([i,j])
    while new_arr:
        a,b = new_arr[0][0], new_arr[0][1]
        del new_arr[0]
        for i in range(4):
            ni = a + dx[i]
            nj = b + dy[i]
            if 0 <= ni < n and 0 <= nj < m:
                if arr2[ni][nj] == 0 :
                    arr2[ni][nj] = 2
                    new_arr.append([ni,nj])
    for i in arr2:
        for j in i:
            if j == 0 :
                result += 1
    cnt = max(cnt, result)

def wall(x):
    if x == 3 :
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                arr[i][j] = 1
                wall(x+1)
                arr[i][j] = 0

wall(0)
print(cnt)

##############################################
import sys
import copy
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]
n, m = map(int,input().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
q = deque()

def wall(x):
    if x == 3 :
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                arr[i][j] = 1
                wall(x+1)
                arr[i][j] = 0

def bfs():
    global cnt
    w = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 :
                q.append([i,j])
    while q :
        x,y = q.popleft()
        for i in range(4):
            ni = x + dx[i]
            nj = y + dy[i]
            if 0 <= ni < n and 0 <=nj < m:
                if w[ni][nj] == 0 :
                    w[ni][nj] = 2
                    q.append([ni,nj])
    total = 0
    for i in w :
        total += i.count(0)

    cnt = max(cnt,total)

wall(0)
print(cnt)