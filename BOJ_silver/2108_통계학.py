from collections import Counter
import sys

N = int(input())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline().strip()))
num.sort()

# 산술평균
avg = round(sum(num) / N)
print(avg)

# 중앙값
cen = num[len(num)//2]
print(cen)

# 최빈값
nums = Counter(num).most_common()
if len(num)>1:
    if nums[0][1] == nums[1][1]: # 최빈값이 두 개 이상일경우
        print(nums[1][0]) # 두번째로 작은 값 출력
    else:
        print(nums[0][0])  # 첫번째값 출력
else:
    print(nums[0][0])

# 범위
min_max = num[-1]-num[0]
print(min_max)
