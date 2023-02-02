N = int(input())
cnt = 0
for i in range(1,N+1):
    x = str(i)
    divide = 0
    for j in x:
        divide += int(j)
    if not i % divide :
        cnt += 1
print(cnt)

#########################
n = int(input())
cnt = 0
a = [0]*(n+1)
for i in range(1, n+1):
    a[i] = a[i//10]+i%10
    if not i % a[i]:
        cnt += 1
print(cnt)