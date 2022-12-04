N = int(input())
cnt = 0
for i in range(1,N+1):
    x = str(i)
    cnt += x.count('3')
    cnt += x.count('6')
    cnt += x.count('9')
print(cnt)