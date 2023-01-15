N = int(input())
lst = list(map(int,input().split()))
cnt = [0]
for i in range(N):
    if lst[i] == 1 :
        cnt.append(cnt[i]+1)
    else :
        cnt.append(cnt[i]-1)
print(max(cnt)-min(cnt))