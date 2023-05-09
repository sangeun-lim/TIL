a,b = map(int,input().split())
c,d = map(int,input().split())
if c >= b or d <= a:
    print(b - a + d - c)
else:
    print(max(b,d) - min(a,c))

#-------------------------------#

a,b = map(int,input().split())
c,d = map(int,input().split())
cnt = 0
lst = [0] * 101

for i in range(a,b):
    lst[i]=1
for i in range(c,d):
    lst[i]=1

for i in range(101):
    if lst[i]:
        cnt += 1

print(cnt)