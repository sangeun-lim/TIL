n = int(input())
for i in range(n):
    k = int(input())
    cnt = 0
    for j in range(k):
        lst = list(map(str,input().split()))
        cnt += float(lst[1]) * float(lst[2])
    print(f'${cnt:.2f}')