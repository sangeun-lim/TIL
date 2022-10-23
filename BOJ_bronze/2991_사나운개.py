a,b,c,d = map(int,input().split())
p,m,n = map(int,input().split())
cnt1 = cnt2 = cnt3 = 0
e = a+b
f = c+d
if 0 < p % e <= a :
    cnt1 += 1
if 0 < p % f <= c:
    cnt1 += 1

if 0 < m % e <= a :
    cnt2 += 1
if 0 < m % f <= c :
    cnt2 += 1

if 0 < n % e <= a :
    cnt3 += 1
if 0 < n % f <= c :
    cnt3 += 1
print(cnt1)
print(cnt2)
print(cnt3)
