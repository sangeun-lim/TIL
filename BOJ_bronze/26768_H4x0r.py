import sys
input = sys.stdin.readline

A = input()
A = A.replace('a','4')
A = A.replace('e','3')
A = A.replace('i','1')
A = A.replace('o','0')
A = A.replace('s','5')
print(A)

############################
trans = {'a':'4','e':'3','i':'1','o':'0','s':'5'}
l = input()
for k, v in trans.items():
    l = l.replace(k, v)
print(l)