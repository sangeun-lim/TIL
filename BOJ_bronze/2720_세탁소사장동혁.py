n = int(input())
for i in range(n):
    dic = {'25' : 0, '10': 0, '5':0, '1':0 }
    x = int(input())
    for j in dic.keys():
        y = x // int(j)
        x = x % int(j)
        dic[j] = y
    print(*dic.values())