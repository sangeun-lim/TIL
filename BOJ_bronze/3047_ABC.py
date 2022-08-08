lst = list(map(int,input().split()))
x = input()
lst.sort()

for i in x :
    if i == 'A':
        print(lst[0], end= ' ')
    elif i == 'B':
        print(lst[1], end= ' ')
    else:
        print(lst[2], end= ' ')