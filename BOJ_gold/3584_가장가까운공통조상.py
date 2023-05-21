import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    par = [0 for _ in range(n+1)]

    for i in range(n-1):
        a, b = map(int,input().split())

        par[b] = a

    x,y = map(int,input().split())

    arr = [] # x의 조상리스트, 자기 자신도 포함시켜야함
    while x != 0:
        arr.append(x)
        x = par[x]

    arr2 = [] # y의 조상리스트
    while y != 0:
        arr2.append(y)
        y = par[y]

    idx1 = len(arr) - 1
    idx2 = len(arr2) - 1

    while idx1 >= 0 and idx2 >= 0 and arr[idx1] == arr2[idx2]:
        idx1 -= 1
        idx2 -= 1

    print(arr[idx1 + 1])
