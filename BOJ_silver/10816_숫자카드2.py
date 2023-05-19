# import sys
#
# M = int(input())
# M_card = list(map(int,sys.stdin.readline().split()))
# N = int(input())
# N_card = list(map(int,sys.stdin.readline().split()))
#
# cnt = [0] * N
# for i in range(N):
#     if N_card[i] in M_card:
#         cnt[i] = M_card.count(N_card[i])
#
# print(*cnt)
#시간초과

#=====================================================#
import sys

M = int(input())
M_card = list(map(int,sys.stdin.readline().split()))
N = int(input())
N_card = list(map(int,sys.stdin.readline().split()))

cnt = {}
for card in M_card:
    if card in cnt:
        cnt[card] += 1
    else :
        cnt[card] = 1

ans = []
for card in N_card:
    temp = cnt.get(card)
    if temp != None:
        ans.append(temp)
    else:
        ans.append(0)

print(*ans)

#---------------------------------------------------#
# 시간초과
# pypy3로 제출

import sys
input = sys.stdin.readline

M = int(input())
M_card = sorted(list(map(int,input().split())))
N = int(input())
N_card = list(map(int,input().split()))

for i in N_card:
    # 인덱스의 제일 왼쪽 인덱스
    idx = 1
    s = 0
    e = M -1
    while s <= e:
        mid = (s+e) // 2

        if M_card[mid] == i:
            idx = mid
            e = mid - 1
        elif M_card[mid] < i:
            s = mid + 1
        else:
            e = mid - 1

    # 인덱스의 제일 오른쪽 인덱스
    idx2 = 0
    s = 0
    e = M -1
    while s <= e:
        mid = (s+e) // 2

        if M_card[mid] == i:
            idx2 = mid
            s = mid + 1
        elif M_card[mid] < i:
            s = mid + 1
        else:
            e = mid - 1

    print(idx2 - idx + 1, end = ' ')