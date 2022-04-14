N,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
cnt = 0
arr.sort(reverse=True)

for i in arr:
    if K // int(i) :
        cnt += K // int(i)
        K = K % int(i)
print(cnt)