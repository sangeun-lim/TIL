N = int(input())
people = list(map(int,input().split()))
people.sort()

total = 0
for i in range(1,len(people)+1):
    for j in people[:i]:
        total += j
print(total)