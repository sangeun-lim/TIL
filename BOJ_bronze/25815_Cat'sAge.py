y,m = map(int,input().split())
a = b = 0
if y < 1 :
    a = m * 15 // 12
    b = m * 15 % 12
elif y < 2 :
    a = 15 + m * 9 // 12
    b = m * 9 % 12
else :
    a = 15 + 9 + (y-2)*4 + m * 4 // 12
    b = m * 4 % 12
print(a,b)