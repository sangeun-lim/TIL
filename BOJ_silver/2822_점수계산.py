lst = []
for i in range(1,9):
    n = int(input())
    lst.append((n,i))

lst.sort(reverse=True)

res = []
total = 0
for i in lst[:5]:
    total += i[0]
    res.append(i[1])
print(total)
res.sort()
print(*res)
