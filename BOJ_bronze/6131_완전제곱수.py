n = int(input())
cnt = 0

# for i in range(1,n):
for i in range(1,501):
    for j in range(1,501):
        if j**2 - i**2 == n:
            cnt += 1
print(cnt)