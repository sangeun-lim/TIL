N, K = map(int,input().split())
lst = []
for i in range(1,N+1):
    if N % i == 0:
        lst.append(i)
    if len(lst) == K:
        break
if K > len(lst):
    print(0)
else:
    print(lst[K-1])

####################################
N, K = map(int,input().split())
cnt = 0
for i in range(1,N+1):
    if N % i == 0 :
        cnt += 1
        if cnt == m :
            print(i)
            break
if cnt < m :
    print(0)