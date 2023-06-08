n = int(input())
arr = list(map(int,input().split()))
arr.sort()
x = len(arr)
if x % 2: # 홀수개면
    print(arr[x//2])
else:
    print(arr[x//2-1])