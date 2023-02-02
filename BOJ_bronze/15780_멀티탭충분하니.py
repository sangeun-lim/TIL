N, K = map(int,input().split())
cnt = 0
lst = list(map(int,input().split()))
for i in lst:
    if i % 2 :
        cnt += i // 2 + 1
    else:
        cnt += i// 2
if cnt >= N :
    print('YES')
else:
    print('NO')

