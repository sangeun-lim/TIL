A = int(input())
B = int(input())
C = int(input())

D = A * B * C
D = str(D)

cnt = [0 for i in range(10)]

for i in D:
    cnt[int(i)] += 1

for i in cnt:
    print(i)