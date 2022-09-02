N,L = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
lst2 = lst[:]
for i in lst2:
    if i <= L :
        L += 1
        lst.remove(i)
print(L)