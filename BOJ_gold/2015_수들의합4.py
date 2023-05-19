# 연속부분수열 문제 --> 투포인터 or 누적합

n,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0 for _ in range(n+1)]
dict = {}

for i in range(1,n+1):
    prefix[i] = prefix[i-1] + arr[i]

ans = 0
for i in range(n+1):
    # ans +=  dict[prefix[i] - k]
    # dict[prefix[i]] += 1

    ans += dict.get(prefix[i] - k, 0)
    dict[prefix[i]] = dict.get(prefix[i], 0) + 1

print(ans)