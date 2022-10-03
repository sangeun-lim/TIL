n = int(input())
p = int(input())
if n < 5:
    print(p)
elif n < 10 :
    if p-500 < 0 :
        print(0)
    else:
        print(p-500)
elif n < 15 :
    if int(min(p - 500,p * 0.9)) < 0:
        print(0)
    else:
        print(int(min(p - 500,p * 0.9)))
elif n < 20 :
    if int(min(p - 2000, p * 0.9)) < 0 :
        print(0)
    else:
        print(int(min(p - 2000, p * 0.9)))
else :
    if int(min(p - 2000, p * 0.75)) < 0 :
        print(0)
    else :
        print(int(min(p - 2000, p * 0.75)))

#=========================================
n = int(input())
p = int(input())
ans=p
if n>=5:
    ans=min(max(p-500,0),ans)
if n>=10:
    ans=min(max(p//100*90,0),ans)
if n>=15:
    ans=min(max(p-2000,0),ans)
if n>=20:
    ans=min(max(p//100*75,0),ans)
print(ans)