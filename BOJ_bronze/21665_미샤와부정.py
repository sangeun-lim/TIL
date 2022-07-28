n,m = map(int,input().split())
lst = list(input() for _ in range(n))
x = input()
lst2 = list(input() for _ in range(n))
total = 0

lst3 = []
lst4 = []
for i in lst:
    for j in i:
        lst3.append(j)
for i in lst2:
    for j in i:
        lst4.append(j)

for i in range(len(lst3)):
    if lst3[i] == lst4[i]:
        total += 1
print(total)

###############################################

n,m = map(int,input().split())
lst = list(input() for _ in range(n))
x = input()
lst2 = list(input() for _ in range(n))
total = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == lst2[i][j]:
            total += 1
print(total)