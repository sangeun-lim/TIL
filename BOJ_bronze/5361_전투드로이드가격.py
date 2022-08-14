t = int(input())
for tc in range(t):
    a,b,c,d,e = map(int,input().split())
    x = a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90
    print(f'${x:0.2f}')