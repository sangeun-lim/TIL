n = int(input())
for i in range(n):
    lst = list(map(str,input().split()))
    res = lst[0][0:int(lst[1])] + lst[0][int(lst[2]):]
    print(res)