while True:
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    if lst[0] == lst[1] == lst[2] == 0:
        break
    else:
        if lst[0] >= lst[1] + lst[2] :
            print('Invalid')
        elif lst[0] == lst[1] == lst[2] :
            print('Equilateral')
        elif lst[0] == lst[1] or lst[0] == lst[2] or lst[1] == lst[2] :
            print('Isosceles')
        elif lst[0] != lst[1] != lst[2]:
            print('Scalene')