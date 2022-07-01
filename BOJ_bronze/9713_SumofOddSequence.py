n = int(input())
for i in range(n):
    x = int(input())
    print(sum([n for n in range(1,x+1) if n % 2]))

#############
n=int(input())
for i in range(n):
    mySum = 0
    a = int(input())
    for x in range(1,a+1):
        if x % 2 != 0:
            mySum += x
    print(sum)