T = int(input())
for tc in range(T):
    x = int(input())
    lst = []
    while x != 0 :
        lst.append(x%2)
        x = x // 2
    for i in range(len(lst)):
        if lst[i] == 1 :
            print(i, end=" ")