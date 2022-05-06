T = int(input())
for tc in range(T):
    arr = list(map(int,input().split()))
    arr2 = sorted(arr)

    print(arr2[-3])
