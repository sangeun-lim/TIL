N = int(input())
cnt = 0
for i in range(N):
    x = input()
    x = int(x[2:])
    if x <= 90:
        cnt += 1
print(cnt)