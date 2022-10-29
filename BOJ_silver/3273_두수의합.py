n = int(input())
num = list(map(int,input().split()))
x = int(input())

num.sort()

s = 0
e = n - 1

cnt = 0

while s < e:
    if num[s] + num[e] == x:
        cnt +=1
        s += 1

    elif num[s] + num[e] > x :
        e -= 1
    else :
        s += 1

print(cnt)