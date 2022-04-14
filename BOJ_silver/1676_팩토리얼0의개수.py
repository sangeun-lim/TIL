N = int(input())
total = 1
cnt = 0

if N == 0 or N == 1:
    print(0)
    exit()
else :
    for i in range(N,0,-1):
        total *= i
total = (str(total))[::-1]

for i in total:
    if i == '0' :
        cnt += 1
    else :
        break
print(cnt)
