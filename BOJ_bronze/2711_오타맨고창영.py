T = int(input())
for i in range(T):
    x,y = input().split()
    x = int(x)
    print(y[:x-1]+y[x:])