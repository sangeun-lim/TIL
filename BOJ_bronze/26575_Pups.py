n = int(input())
for i in range(n):
    x, y, z = map(float, input().split())
    print(f'${x * y * z:.2f}')
