lst = []
for i in range(1,31):
    lst.append(i)

for i in range(28):
    x = int(input())
    lst.remove(x)
print(lst[0])
print(lst[1])