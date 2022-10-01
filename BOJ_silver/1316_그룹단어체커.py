N = int(input())
result = N
for i in range(N):
    x = input()
    for j in range(len(x)-1):
        if x[j] == x[j+1]:
            pass
        elif x[j] in x[j+1:]:
            result -= 1
            break
print(result)
