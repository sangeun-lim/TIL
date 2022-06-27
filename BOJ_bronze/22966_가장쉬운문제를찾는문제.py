N = int(input())
dic = {}
for i in range(N):
    lst = input().split()
    if lst[0] not in dic :
        dic[lst[0]] = lst[1]
x = min(dic.values())
for i,j in dic.items() :
    if x == j :
        print(i)
        break