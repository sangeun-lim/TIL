# 시간초과
M = int(input())
N = int(input())
arr = []

while M != N :
    cnt = 0
    for i in range(1,N+1):
        if M % i == 0 :
            cnt += 1
    if cnt == 2 :
        arr.append(M)
    M += 1

if len(arr) > 0 :
    print(sum(arr))
    print(arr[0])
else:
    print(-1)

########################

M = int(input())
N = int(input())
arr = []

for i in range(M,N+1):
    cnt = 0
    if i > 1 :
        for j in range(2,i):
            if i % j == 0 :
                cnt += 1
                break
        if cnt == 0 :
            arr.append(i)
            
if len(arr) > 0 :
    print(sum(arr))
    print(arr[0])
else:
    print(-1)