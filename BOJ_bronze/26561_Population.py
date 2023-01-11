n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    die = y // 7
    birth = y // 4
    print(x+birth-die)