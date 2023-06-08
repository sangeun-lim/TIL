import sys
input = sys.stdin.readline

n = int(input())
arr = [(int(input())) for _ in range(n)]
arr.sort()
arr = arr[::-1]

mx = 0
for i in range(n):
    mx = max(mx, arr[i]*(i+1))
print(mx)