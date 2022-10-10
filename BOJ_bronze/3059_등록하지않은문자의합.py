t = int(input())
for i in range(t):
    s = input()
    total = 2015
    s = set(s)
    for j in s:
        total -= ord(j)
    print(total)