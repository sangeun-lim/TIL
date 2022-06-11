N = int(input())
cnt = 0
lst = list(map(int,input().split()))
want = int(input())
for i in lst:
    if i == want:
        cnt += 1
print(cnt)