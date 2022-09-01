n = int(input())
x1 = input()
x2 = input()

result = 0
for i in range(n):
    if x1[i] != x2[i] :
        result += 1
print(result)