n,m,k = map(int,input().split())
x = min((n+m-k)//3 , m , n//2)
print(x)

###############################

n,m,k = map(int,input().split())
res = 0
while True:
    n -= 2
    m -= 1
    if n < 0 or m < 0 or n + m < k :
        break
    res += 1
print(res)

################################
n,m,k = map(int,input().split())
people = n+m+k
team = people // 3
cnt = 0

for i in range(team):
    if n >= 2 and m >= 1:
        n -= 2
        m -= 1
        cnt += 1
    else :
        break
print(cnt)

##################################
n,m,k = map(int,input().split())
x = min(n//2, m)
x = min(x, (n+m-k)//3)
print(x)