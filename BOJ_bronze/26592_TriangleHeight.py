n = int(input())
for i in range(n):
    area,base = map(float,input().split())
    height = area * 2 / base
    print(f'The height of the triangle is {height:.2f} units')