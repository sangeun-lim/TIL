# import sys
# N = int(input())
# sorted_member = []
# member = [list(map(str,sys.stdin.readline().split())) for _ in range(N)]
#
# for i in range(N-1,0,-1):
#     for j in range(i):
#         if int(member[j][0]) > int(member[j+1][0]):
#             member[j][0],member[j+1][0] = member[j+1][0], member[j][0]
#             member[j][1],member[j+1][1] = member[j+1][1], member[j][1]
#
# for i in range(N):
#     print(f'{member[i][0]} {member[i][1]}')
# 시간초과

#-------------------------------------------------------------------#
# import operator
import sys
N = int(input())
member = []
for i in range(N):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)
    member.append((age,name))

#member.sort(key=lambda x: x[0])
member = sorted(member, key=lambda x: x[0])

for i in range(N):
    print(f'{member[i][0]} {member[i][1]}')