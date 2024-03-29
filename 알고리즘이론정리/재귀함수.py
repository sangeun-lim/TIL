# 재귀 함수
# 반복으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성
    return n * factorial_recursive(n - 1)
print(factorial_iterative(5))
print(factorial_recursive(5))