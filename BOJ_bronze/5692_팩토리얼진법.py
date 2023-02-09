import sys

input = sys.stdin.readline
while True:
    x = int(input())
    if x == 0:
        break
    else:
        res = 0
        fact = [1, 2, 6, 24, 120]
        lst = []
        x = str(x)
        for i in x[::-1]:
            lst.append(i)
        for i in range(len(lst)):
            res += (int(lst[i]) * fact[i])
        print(res)

###############################################
import math
import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if not n:
        break
    x, i = 0, 1
    while n:
        x += (n % 10) * math.factorial(i)
        n //= 10
        i += 1
    print(x)

