T = int(input())
for i in range(T):
    x, y = map(str,input().split())
    for i in range(1,int(x)+1):
        print(y*i)
        y = ord(y) + 1
        if y == 91:
            y = 65
        y = chr(y)
    print()

#--------------------------------------#
for _ in range(int(input())):
    n, a = input().split()
    n, a = int(n), ord(a)
    for i in range(1, n + 1):
        print(chr(a) * i)
        a += 1
        if a == 91:
            a -= 26
    print()

