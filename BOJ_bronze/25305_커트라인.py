N, k = map(int,input().split())
x = N-k
lst = list(map(int,input().split()))
lst.sort()
print(lst[x])