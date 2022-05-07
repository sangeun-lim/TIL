a,b = map(int,input().split())
if a % 4 == 1 :
    x1 = 0
elif a % 4 == 2:
    x1 = 1
elif a % 4 == 3:
    x1 = 2
else :
    x1 = 3

if b % 4 == 1 :
    x2 = 0
elif b % 4 == 2:
    x2 = 1
elif b % 4 == 3:
    x2 = 2
else :
    x2 = 3

if a % 4 == 0 :
    y1 = a // 4 - 1
else :
    y1 = a // 4

if b % 4 == 0 :
    y2 = b // 4 - 1
else :
    y2 = b // 4

x = abs(x1-x2)
y = abs(y1-y2)
print(x+y)

##########################
a,b=map(int,input().split())
a-=1;b-=1
print(abs(a//4-b//4)+abs(a%4-b%4))

#################################
a,b = map(int,input().split())

v1 = a // 4 if a % 4 != 0 else a // 4 - 1
v2 = b // 4 if b % 4 != 0 else b // 4 - 1

v3 = a % 4 if a % 4 != 0 else 4
v4 = b % 4 if b % 4 != 0 else 4

x = abs(v1-v2)
y = abs(v3-v4)
print(x+y)