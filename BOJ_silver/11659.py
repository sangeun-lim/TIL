n, m = map(int,input().split()) # n= 수의 개수, m= 구해야하는 횟수
num = list(map(int,input().split()))
for tc in range(m):
    nn,mm = map(int,input().split())
    total = 0
    for j in range(nn,mm+1):
        total += num[j-1]
    print(total)
###############################################
import sys
input =  sys.stdin.readline
n, m = map(int,input().split()) # n= 수의 개수, m= 구해야하는 횟수
num = list(map(int,input().split()))
for tc in range(m):
    nn,mm = map(int,input().split())
    total = 0
    for j in range(nn,mm+1):
        total += num[j-1]
    print(total)
#########################################
import sys
input =  sys.stdin.readline
n, m = map(int,input().split()) # n= 수의 개수, m= 구해야하는 횟수
num = list(map(int,input().split()))
prefix_sum = [0]

temp = 0
for i in num :
    temp += i
    prefix_sum.append(temp)
for tc in range(m):
    nn, mm = map(int, input().split())
    print(prefix_sum[mm]-prefix_sum[nn-1])
