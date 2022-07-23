import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))

# 최대 공약수
def GCD(a,b) : # a가 큰 수
    while b != 0:
        x = a % b
        a = b
        b = x
    return a

for i in range(1,n):
    num = GCD(lst[0], lst[i])
    print(f'{lst[0]//num}/{lst[i]//num}')


#########################################################

n=int(input())
lst=list(map(int, input().split()))

for i, b in enumerate(lst[1:]):
    a=lst[0]
    while b!=0:
        a,b=b,a%b
    print(f'{lst[0]//a}/{lst[i+1]//a}')

#######################################################
import math
N = int(input())
numbers = list(map(int, input().split()))
best = numbers[0]
for i in range(1, N):
    print(f'{best // math.gcd(best, numbers[i])}/{numbers[i]//math.gcd(best, numbers[i])}')
