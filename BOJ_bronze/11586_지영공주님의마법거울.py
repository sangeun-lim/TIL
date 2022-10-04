n = int(input())
lst = []
for i in range(n):
    lst.append(input())
k = int(input())
if k == 1 :
    for i in lst:
        print(i)
elif k == 3 :
    for i in range(len(lst)-1,-1,-1):
        print(lst[i])
else :
    for i in lst:
        print(i[::-1])