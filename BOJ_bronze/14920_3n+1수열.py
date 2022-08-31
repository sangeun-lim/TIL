cnt = 1
n = int(input())
while n != 1 :
    if n % 2 :
        n = 3 * n + 1
        cnt += 1
    else:
        n = n // 2
        cnt += 1
print(cnt)
