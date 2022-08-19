import sys
input = sys.stdin.readline

n = int(input())
a = b = 0
for i in range(n):
    x,y = map(int,input().split())
    if x > y :
        a += 1
    elif x < y :
        b += 1
    else :
        pass
print(f'{a} {b}')