ds, ys = map(int,input().split())
dm, ym = map(int,input().split())

x = ys-ds
y = ym-dm

sun_list = []
moon_list = []

for i in range(x,5001,ys):
    sun_list.append(i)
for i in range(y,5001,ym):
    moon_list.append(i)

for i in sun_list:
    if i in moon_list:
        print(i)
        break

#------------------------------------#
import sys
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
n = 0
while True:
    a, c, n = (a + 1) % b, (c + 1) % d, n + 1
    if a + c == 0:
        break
print(n)