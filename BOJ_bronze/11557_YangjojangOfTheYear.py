T = int(input())
for tc in range(T):
    n = int(input())
    dic = {}
    for i in range(n):
        lst = list(input().split())
        dic[lst[0]] = lst[1]

    max_dic = 0
    for i in dic.values():
        max_dic = max(max_dic,int(i))

    for k,v in dic.items():
        if int(v) == max_dic:
            print(k)