N = int(input())
num = list(map(int,input().split()))

ans = 0

mx = num[0]
ans = num[0]
for i in range(1,N):
    mx = max(mx+num[i], num[i]) # 개수가 늘어날때마다 계산하는 최대값
    ans = max(mx,ans)           # 전체 최대값

print(ans)