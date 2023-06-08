import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

total = 0
for i in range(n):
    if total + 1 >= arr[i]:
        total += arr[i]
    else:
        break
print(total + 1)
