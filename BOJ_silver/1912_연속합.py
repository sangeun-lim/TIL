N = int(input())
num = list(map(int,input().split()))

ans = 0

mx = num[0]
ans = num[0]
for i in range(1,N):
    mx = max(mx+num[i], num[i])
    ans = max(mx,ans)

print(ans)