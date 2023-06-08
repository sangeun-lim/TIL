import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

i = n
cnt = 0

while i != 0:
    if arr[i] <= arr[i-1]:
        arr[i-1] -= 1
        cnt += 1
    else:
        i -= 1
print(cnt)