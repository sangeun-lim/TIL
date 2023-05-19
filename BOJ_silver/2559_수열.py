n,k = map(int,input().split())
arr = [0] + list(map(int,input().split()))

prefix = [0 for _ in range(n+1)]
for i in range(1,n+1): # 누적합배열
    prefix[i] = prefix[i-1] + arr[i]

ans = -10000000000

for i in range(k,n+1):
    ans = max(ans, prefix[i] - prefix[i-k])

print(ans)