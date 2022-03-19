N = int(input())
min_num = 1000001

a = []
for i in range(1,1000001):
    if i < 10 :
        if N == i+i:
            a.append(i)
    elif i < 100 :
        if N == i + i % 10 + i // 10:
            a.append(i)
    elif i < 1000 :
        if N == i + i // 100 + i % 100 // 10 + i % 100 % 10 :
            a.append(i)
    elif i < 10000 :
        if N == i + i // 1000 + i % 1000 // 100 + i % 1000 % 100 // 10 + i % 1000 % 100 % 10:
            a.append(i)
    elif i < 100000 :
        if N == i + i // 10000 + i % 10000 // 1000 + i % 10000 % 1000 // 100 + i % 10000 % 1000 % 100 // 10 + i % 10000 % 1000 % 100 % 10:
            a.append(i)
    elif i < 1000000 :
        if N == i + i // 100000 + i % 100000 // 10000 + i % 100000 % 10000 // 1000 + i % 100000 % 10000 % 1000 // 100 + i % 100000 % 10000 % 1000 % 100 // 10 + i % 100000 % 10000 % 1000 % 100 % 10:
            a.append(i)

if len(a) > 0 :
    print(min(a))
else :
    print(0)

#############################
# 다른 사람 풀이
M = 0
N = int(input())
total = 0

for i in range(1, N):
    total = i
    strN = str(i)
    for d in strN:
        total += int(d)
    if total == N:
        M = i
        break

print(M)

########################
# 다른 사람 풀이 2


N = int(input())

for i in range(1,N+1):
    Num = sum((map(int,str(i))))
    Num_Sum = i + Num
    if Num_Sum == N:
        print(i)
        break
    if i == N:
        print('0')