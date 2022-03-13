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