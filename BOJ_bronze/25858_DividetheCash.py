n,d = map(int,input().split())
lst = []
for i in range(n):
    lst.append(int(input()))
total = sum(lst)
x = d // total

for i in lst:
    print(i*x)