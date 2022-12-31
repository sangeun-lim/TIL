n = int(input())
for i in range(n):
    x,y = map(float,input().split())
    z = abs(x-y)
    print(f'{z:.1f}')