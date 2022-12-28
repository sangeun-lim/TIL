n = int(input())
for i in range(n):
    x = input()
    res = x[0]
    for j in range(1,len(x)):
        if x[j-1] != x[j] :
            res += x[j]
    print(res)