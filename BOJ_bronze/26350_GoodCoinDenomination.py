T = int(input())
for i in range(T):
    x, *lst = map(int,input().split())
    print(f'Denominations: ', end='')
    print(*lst)
    for j in range(1,x):
        if lst[j-1] * 2 <= lst[j]:
            continue
        else :
            print('Bad coin denominations!')
            break
    else:
        print('Good coin denominations!')
    print()

