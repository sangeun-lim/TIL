C = int(input())
for i in range(C):
    x = int(input())
    total = 0
    for j in range(1,x+1):
        if x % j == 0 :
            total += 1
    print(f'{x} {total}')