# 다이나믹 프로그래밍(동적 계획법)
# 1. 최적부분구조
#    큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제 해결
# 2. 중복되는 부분 문제
#    동일한 작은 문제를 반복적으로 해결
# 탑다운(하향식) 방식(메모이제이션)

# 피보나치 수열: 탑다운 다이나믹 프로그래밍
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
dp = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]
print(fibo(99))

#--------------------------------------------------------------------#

# 피보나치 수열: 바텀업 다이나믹 프로그래밍

dp = [0] * 100

dp[1] = 1
dp[2] = 1
n = 99

#반복문으로 구현
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])

#--------------------------------------------------------------------#

# n x m 형태가 1차원 리스트로 주어졌을 때
# 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
n,m = map(int,input().split())
array = list(map(int,input().split()))
dp = []
index = 0
for i in range(n):
    dp.append(array[index:index + m])
    index += m

#--------------------------------------------------------------------#

# LIS 알고리즘(가장 긴 증가하는 부분 수열)
n = int(input())
arr = list(map(int,input().split()))
dp = [1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i] :
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))