K = int(input())
nums = []
for tc in range(K):
    N = int(input())
    if N != 0 :
        nums.append(N)
    else :
        nums.pop(-1)

print(sum(nums))