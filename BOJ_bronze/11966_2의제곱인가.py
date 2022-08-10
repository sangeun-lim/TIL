N = int(input())
lst = []
for i in range(31):
    lst.append(2**i)
if N in lst:
    print(1)
else:
    print(0)