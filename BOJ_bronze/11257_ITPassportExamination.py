n = int(input())
for i in range(n):
    j , k, l, m = map(int,input().split())
    z = k+l+m
    if k >= 11 and l >= 8 and m >= 12 and z >= 55:
        print(f'{j} {z} PASS')
    else:
        print(f'{j} {z} FAIL')