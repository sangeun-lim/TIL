import sys
input = sys.stdin.readline

N,M,B = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
time = 9999999999999999999999
height = 0

for i in range(257): # 땅의 최대 높이가 256
    mmax = 0
    mmin = 0
    for j in range(N): # 가로
        for k in range(M): # 세로
            if arr[j][k] < i: # 블럭이 현재 높이보다 작으면
                mmin += i - arr[j][k] # 현재 높이가 블록 높이보다 높을 때 ( mmin 만큼 인벤토리에서 꺼내와야 됨)
            else :
                mmax += arr[j][k] - i # 블록높이가 현재높이보다 높을 때 (mmax만큼 인벤토리에 들어감)

    if mmin > mmax + B:
        continue
    t = mmin + mmax*2 # 블록제거 * 2 + 블록 추가
    if t <= time :
        time = t
        height = i
print(time,height)

###############################################
n,m,b = map(int,input().split())
arr_cnt = [0]*257

max_h = 0
min_h = 256
for i in range(n):
    temp = list(map(int,input().split()))
    for j in temp:
        if j > max_h:
            max_h = j
        if j < min_h:
            min_h = j
        arr_cnt[j] += 1
h = min_h
min_time=12800000000
for i in range(min_h,max_h+1):  #목표 높이
    temp = b
    time = 0
    for j in range(min_h,max_h+1):  #땅의 높이
        if i < j:              # 목표 높이보다 땅이 높으면
            time += (j-i)*arr_cnt[j]*2
            temp += (j-i)*arr_cnt[j]
        elif i > j:             #목표 높이보다 땅이 낮으면
            time += (i-j)*arr_cnt[j]
            temp -= (i-j)*arr_cnt[j]
    if temp < 0:
        continue
    if min_time >= time:
        min_time = time
        h = i
print(min_time,h)

###########################
import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1000000000000000000000000000000
for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)

################################################################
from math import inf
import sys

N, M, B = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tall = 0
ans = inf  # 시간초과 방지를 위해 충분히 큰 수로 둠

for i in range(257):  # 땅의 높이의 최대는 256이므로 0 ~ 256까지만 탐색
    max = 0
    min = 0
    for j in range(N):  # 가로
        for k in range(M):  # 세로
            if ground[j][k] < i:  # 블럭이 현재 높이 보다 작다면
                min += (i - ground[j][k])  # 현재 높이가 블록 높이보다 높을 때 (min 만큼 인벤토리에서 꺼내서 채워야 함)

            else:
                max += (ground[j][k] - i)  # 블록 높이가 현재 높이보다 높을 때 (max 만큼 블록이 제거된 후 인벤토리에 들어감)

    inventory = max + B  # 인벤토리에 있는 총 블록수 = 현재 인벤토리에 있는 블록 + max

    if inventory < min:  # 전부 채울 수 없으므로 패스
        continue

    time = 2 * max + min  # 블록 제거는 2초, 블록 추가는 1초

    if time <= ans:  # 높이는 0 ~ 256 까지 오름차순으로 탐색하기 때문에 걸린 시간이 같아도 더 높은 높이가 출력 된다
        ans = time
        tall = i

print(ans, tall)