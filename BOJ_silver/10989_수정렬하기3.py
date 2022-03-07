# import sys
#
# N = int(input())
# num = [int(sys.stdin.readline()) for _ in range(N)]
#
# for i in range(N-1,0,-1):
#     for j in range(i):
#         if num[j] > num[j+1] :
#             num[j+1],num[j] = num[j] , num[j+1]
# for i in num:
#     print(i)
# 위 코드는 메모리 초과

##################################################
import sys

num_list = [0]*10001
N = int(input())
for i in range(N):
    input_num = int(sys.stdin.readline())

    num_list[input_num] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)