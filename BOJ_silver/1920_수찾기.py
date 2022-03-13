N = int(input())
N_num = list(map(int,input().split()))
M = int(input())
M_num = list(map(int,input().split()))

num = {}
for i in N_num:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

ans = []
for i in M_num:
    temp = num.get(i)
    if temp != None:
        ans.append(1)
    else:
        ans.append(0)

for i in ans:
    print(i)

#--------------------------------------#
import sys

n = int(input())
arr = sorted(list(map(int, sys.stdin.readline().split())))
m = int(input())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums:
    p = 0
    q = n-1

    while p <= q:
        mid = (p + q) // 2
        if arr[mid] == num:
            print(1)
            break
        elif arr[mid] < num:
            p = mid + 1
        else:
            q = mid - 1
    else:
        print(0)
