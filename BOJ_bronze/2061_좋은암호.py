# 시간초과
def factorize(n):
    factor = 2 # 시작 소수 지정
    while (factor ** 2 <= n): # 에라토스테네스, 루트 n까지 실행
        while(n % factor == 0): # 소수로 나누어 떨어지면 ( 약수이면 )
            factors.append(factor) # 리스트에 추가
            n = n // factor # n을 몫으로 변경
        factor += 1
    if n > 1 : # 1보다 크고 factor **2 보다  작은 경우 n은 소수임으로 append
        factors.append(n)

K,L = map(int,input().split())
factors = []
factorize(K)
if min(factors) < L :
    print("BAD", min(factors))
else :
    print("GOOD")

#################################################################

# 시간초과
def factorization(x):
    d = 2
    while d <= x :
        if x % d == 0:
            factors.append(d)
            x = x // d
        else :
            d = d + 1

factors = []
K,L = map(int,input().split())
factorization(K)
if min(factors) < L :
    print("BAD" , min(factors))
else :
    print("GOOD")

####################################################
import sys
K,L = sys.stdin.readline().split()

for i in range(2, int(L)):
    if (int(K) % i == 0):
        print("BAD", i)
        exit()
print("GOOD")

##############################################
K,L = map(int,input().split())

for i in range(2,L):
    if K % i == 0 :
        print("BAD", i)
        exit()
print("GOOD")