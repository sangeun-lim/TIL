n, m = map(int, input().split())
cnt = n
while n // m:
    cnt += n // m
    n //= m
print(cnt)