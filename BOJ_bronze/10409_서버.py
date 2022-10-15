n, T = map(int,input().split())
cnt = total = 0
lst = list(map(int,input().split()))
for i in lst:
    total += i
    if total <= T :
        cnt += 1
    else :
        break
print(cnt)