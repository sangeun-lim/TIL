b1,b2 = map(int,input().split())
c1,c2 = map(int,input().split())
d1,d2 = map(int,input().split())

B = max(abs(d1-b1),abs(d2-b2))
D = abs(d1-c1) + abs(d2-c2)

if B > D :
    print('daisy')
elif B < D :
    print('bessie')
else :
    print('tie')