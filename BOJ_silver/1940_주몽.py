N = int(input())
M = int(input())
arr = list(map(int,input().split()))
arr.sort()

s = 0
e = N-1
cnt = 0

while s < e:
    if arr[s] + arr[e] == M:
        cnt += 1
        s += 1
        e -= 1
    elif arr[s] + arr[e] < M :
        s += 1
    else:
        e -= 1

print(cnt)