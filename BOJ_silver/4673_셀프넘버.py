arr = []
for i in range(1,10001):
    arr.append(i)

for i in range(1,10001):
    a = i + i // 1000 + i % 1000 // 100 + i % 1000 % 100 // 10 + i % 1000 % 100 % 10
    if a in arr:
        arr.remove(a)

for i in arr:
    print(i)