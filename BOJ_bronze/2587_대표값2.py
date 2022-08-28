lst = []
for i in range(5):
    x = int(input())
    lst.append(x)
lst.sort()
print(sum(lst)//5)
print(lst[2])