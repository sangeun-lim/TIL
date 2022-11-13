n,c = map(int,input().split())
total = 0
bed = 0
cost = 0
for i in range(n):
    x ,y = input().split()
    total += int(x)
    if y == 'bedroom':
        bed += int(x)
    if y != 'balcony':
        cost += int(x) * c
    else:
        cost += int(x) * 0.5 * c
print(total)
print(bed)
print(f'{cost:.1f}')