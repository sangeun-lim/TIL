a,b = map(int,input().split())
c,d = a//b ,a%b
# print(d)
if a != 0 and d < 0:
    c = c + 1
    d = d-b
print(c)
print(d)