# 소수 판별 알고리즘 : 기본
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2,x):
        # x 가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

print(is_prime_number(4))
print(is_prime_number(7))

#--------------------------------------------------------------------#

# 소수 판별 알고리즘 : 개선
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0 :
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

#--------------------------------------------------------------------#

# 다수의 소수 판별
# 에라토스테네스의 체
# 1. 2부터 N까지 모든 자연수 나열
# 2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i를 찾음
# 3. 남은 수 중에서 i의 배수를 모두 제거 (i는 제거하지 않음)
# 4. 2번과 3번 반복

import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수가 소수(True)인것으로 초기화(0과 1은 제외)
array = [True for i in range(n+1)]

# 에라토스테네스의 체 알고리즘 수행
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')