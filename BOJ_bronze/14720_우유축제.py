N = int(input())
lst = list(map(int,input().split()))
res = []
if lst[0] == 0:
    res.append(lst[0])
for i in range(1,N):
    if len(res) == 0 :
        if lst[i] == 0:
            res.append(lst[i])
    else :
        if lst[i] == 1 and res[-1] == 0:
            res.append(lst[i])
            continue
        elif lst[i] == 2 and res[-1] == 1:
            res.append(lst[i])
            continue
        elif lst[i] == 0 and res[-1] == 2 :
            res.append(lst[i])
            continue
print(len(res))


#################################################
n = int(input())
store = list(map(int, input().split()))
cnt = 0

for i in range(n):
  if store[i] == (cnt % 3):
    cnt += 1

print(cnt)