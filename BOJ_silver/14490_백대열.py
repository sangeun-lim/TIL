# 최대공약수 구하기
def gcd(x,y):
    while y > 0:
        tmp = x
        x = y
        y = tmp % y
    return x

n,m = map(int,input().split(':'))

a = gcd(n,m)
print(f'{n // a}:{m // a}')