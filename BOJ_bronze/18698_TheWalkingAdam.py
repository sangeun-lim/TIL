T = int(input())
for tc in range(T):
    x = input()
    total = 0
    for i in x:
        if i =='U':
            total += 1
        else :
            print(total)
            break
    else :
        print(total)