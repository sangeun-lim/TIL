# a, b = map(int, input().split())
#
# A, B = a, b
# while a % b != 0:
#     a, b = b, a % b
#
# GCD = b               # 최대공약수
#
# LCM = A * B // b      # 최소공배수

# 조건 1. A 와 B 값 중 큰 값이 무조건 작은 값의 배수여야 한다.
# 조건 2. C = (최소공배수 / 최대공약수)를 한뒤
#         곱하면 C 가 나오는 모든 쌍을 뽑고
#         그 쌍들의 합 중 가장 작은 값 두개를 구함
#         A 와 B 중 가장 작은 값과 나온 쌍들을 곱한 값을 출력 한다 .

a, b = map(int, input().split())
c = b // a

def gcd(n,m):           # 최대공약수 구하기
    while m > 0:
        n, m = m , n % m
    return n            # n이 1이 return 되면 n과 m 은 서로소 
    
# c 의 약수를 담을 리스트
c_list = []

for i in range(1,c+1):
    if i * i > c :
        break

    if c % i == 0:
        c_list.append(i)
        c_list.append(c//i)

c_list.sort()
c_len = len(c_list)

for i in range(c_len):
    # c의 약수가 홀수개면
    if len(c_list) % 2 == 1 :
        d = c_list[(len(c_list)//2)]
        print(a*d, a*d)
    # 짝수개면
    else :
        d = c_list[(len(c_list)//2)-1]
        e = c_list[(len(c_list)//2)]
        if gcd(d,e) != 1 : # 서로소가 아니면 삭제
            c_list.remove(d)
            c_list.remove(e)

# 짝수개일때            
if len(c_list) % 2 == 0:
    d = c_list[(len(c_list)//2)-1]
    e = c_list[(len(c_list)//2)]
    print(a*d,a*e)



#########################################################
# 윤혁님 풀이
a, b = map(int, input().split())
c = b // a

for i in range(1,c+1):
    if i * i > c :          # c의 제곱근 이하까지만 계산
        break

    if c % i == 0:
        d = i
        e = c // i
        # d * e == c

        while d % e != 0:          # 서로소를 구하는 연산
            d , e = e , d % e
        if e == 1 :
            x = i
            y = c // i

print(x*a, y*a)

# ##############################################################
# 재민님 풀이
a, b = map(int, input().split())
c = b // a

def gcd(n,m):           # 최대 공약수
    while m > 0:
        n, m = m , n % m
    return n

c_list = []
for i in range(1,c+1):
    if i*i > c:
        break

    if c % i == 0 : 
        c_list.append([i,c//i])  # 공약수들의 짝을 리스트에 저장

for j in range(len(c_list)):
    if gcd(c_list[j][0],c_list[j][1]) != 1: # 서로소가 아니라면
        c_list[j] = 0

while 0 in c_list:
    c_list.remove(0) # 서로소가 아닌 짝은 삭제

print(c_list[-1][0]*a, c_list[-1][1]*a)


#######################################################
# 초기 내 풀이

a, b = map(int, input().split())
c = b // a

# c 의 약수를 담을 리스트
c_list = []

for i in range(1,c+1):
    if c % i == 0:
        c_list.append(i)

# c의 약수가 짝수개면 
if len(c_list) % 2 == 0 :
    d = c_list[(len(c_list)//2)-1]
    e = c_list[(len(c_list)//2)]

    print(a*d, a*e)
else :
    d = c_list[(len(c_list)//2)]
    print(a*d, a*d)

