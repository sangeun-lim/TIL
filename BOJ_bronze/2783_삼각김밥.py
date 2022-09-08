x ,y = map(int,input().split())
res = 1000 / y * x
lst = [res]
n = int(input())
for i in range(n):
    xi, yi = map(int,input().split())
    res = 1000 / yi * xi
    lst.append(res)
print(f'{min(lst):.2f}')
