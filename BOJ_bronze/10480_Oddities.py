N = int(input())
for i in range(N):
    x = int(input())
    y = abs(x)
    if y % 2 == 0 :
        print(f'{x} is even')
    else:
        print(f'{x} is odd')