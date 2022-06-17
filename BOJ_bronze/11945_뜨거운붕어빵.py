n, m = map(int,input().split())
lst = []
for i in range(n):
    x = input()
    lst.append(x)
for i in lst:
    print(i[::-1])