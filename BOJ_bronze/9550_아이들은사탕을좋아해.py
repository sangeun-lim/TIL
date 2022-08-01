T = int(input())
for i in range(T):
    N, K = map(int,input().split())
    total = 0
    lst = list(map(int,input().split()))
    for k in lst:
        total += k // K

    print(total)