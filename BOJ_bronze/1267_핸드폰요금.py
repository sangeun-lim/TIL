N =int(input())
arr =  list(map(int,input().split()))

Y = 0
M = 0

for i in arr :
    if i % 30 == 0 :
        Y += (i//30 +1) * 10
    else :
        Y += ((i+29)//30) * 10

for i in arr:
    if i % 60 == 0 :
        M += (i//60 +1) * 15
    else:
        M += ((i+59)//60) * 15

if Y < M :
    print(f'Y {Y}')
elif Y > M :
    print(f'M {M}')
else:
    print(f'Y M {Y}')