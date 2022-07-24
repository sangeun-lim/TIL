T = int(input())
for tc in range(T):
    x = list(map(int,input().split()))
    x.sort()
    x.pop(4)
    x.pop(0)
    if x[2] - x[0] >= 4:
        print('KIN')
    else:
        print(sum(x))