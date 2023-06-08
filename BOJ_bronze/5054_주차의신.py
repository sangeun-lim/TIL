t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    x = (max(arr) - min(arr)) * 2
    print(x)