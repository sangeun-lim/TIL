n = int(input())
print('Gnomes:')
for i in range(n):
    x,y,z = map(int,input().split())
    if x <= y<= z or z<=y<=x:
        print('Ordered')
    else:
        print('Unordered')