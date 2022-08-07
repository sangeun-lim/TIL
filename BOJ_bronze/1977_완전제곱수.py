M = int(input())
N = int(input())
total = []

for i in range(M,N+1):
    x =  int(i ** 0.5)
    if i == x ** 2 :
        total.append(i)
if len(total) > 0 :
    print(sum(total))
    print(total[0])
else:
    print(-1)
