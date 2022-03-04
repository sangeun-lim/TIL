from math import factorial
n, k = map(int, input().split())
a = factorial(n) // (factorial(k) * factorial(n - k))
print(a)

# nCk == nCn-k

n, k = map(int,input().split())
num1 = 1
num2 = 1

for i in range(n,n-k,-1):
    num1 = num1 * i

for i in range(1,k+1):
    num2 = num2 * i
print(num1//num2)