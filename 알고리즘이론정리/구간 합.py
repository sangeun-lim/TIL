# 구간 합(접두사 합(prefix sum) 이용하기)
n = 5
data = [10,20,30,40,50]

# 접두사 합(prefix sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])