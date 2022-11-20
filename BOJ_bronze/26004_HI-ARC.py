dic = {'H':0, 'I': 0, 'A': 0, 'R': 0, 'C': 0}
x = int(input())
y = input()
for i in y:
    if i in dic:
        dic[i] += 1
print(min(dic.values()))

#############
from collections import Counter
n=int(input())
s=Counter(input())
h,i,a,r,c=s['H'],s['I'],s['A'],s['R'],s['C']
print(min(h,i,a,r,c))