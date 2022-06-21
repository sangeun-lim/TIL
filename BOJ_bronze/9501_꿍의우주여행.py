T = int(input())
for tc in range(T):
    N, D = map(int,input().split())
    cnt = 0
    for i in range(N):
        v,f,c= map(int,input().split())
        if v * (f/c) >= D :
            cnt += 1
    print(cnt)