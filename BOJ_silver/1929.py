# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

M, N = map(int,input().split())


for i in range(M, N+1):
    if i == 1: # 1은 소수가 아님
        continue
    for j in range(2, int(i ** 0.5)+1): # 마지막 값의 제곱근까지만 나눠보면 됨 why? ==> 약수는 대칭이기 때문 
        if i % j == 0:                  
            break
    else :
        print(i)


# ===================================================
# 이전 코드
m, n = map(int,input().split())
my_list = []

for i in range(m,n+1):
    if i == 1:
        pass
    elif i == 2 :
        my_list.append(i)
    else:
        for j in range(2,i):
            if i % j == 0:
                break
            elif j == i-1:
                my_list.append(i)



for i in range(len(my_list)):
    print(my_list[i])
        