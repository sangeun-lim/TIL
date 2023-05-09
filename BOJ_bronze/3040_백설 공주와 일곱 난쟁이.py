lst = []
for i in range(9):
    lst.append(int(input()))
x = sum(lst)
y = x - 100
res = []
for i in range(8):
    for j in range(i+1,8):
        if lst[i] + lst[j] == y:
            res.append(lst[i])
            res.append(lst[j])
            break
for i in lst:
    if i not in res:
        print(i)

#--------------------------------#
import sys
from itertools import combinations
input=sys.stdin.readline
a=[]
for i in range(9):
    a.append(int(input()))

for i in combinations(a,7):
    if sum(i)==100:
        for j in i:
            print(j)

####################################

lst = []
for _ in range(9):
    lst.append(int(input()))
x = sum(lst)
y = x - 100
flag = 0
for i in range(8):
    for j in range(i+1,9):
        if lst[i] + lst[j] == y:
            flag = 1
            a, b = lst[i], lst[j]
            break
    if flag:
        break

lst.remove(a)
lst.remove(b)

for i in lst:
    print(i)
