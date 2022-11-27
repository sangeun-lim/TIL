
n = int(input())
total = 0
lst = list(map(float,input().split()))
for i in lst:
    total += i**3
print(total**(1/3))