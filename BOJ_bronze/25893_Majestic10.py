n = int(input())
for i in range(n):
    x,y,z = map(int,input().split())
    print(x,y,z)
    cnt = 0
    if x >= 10 :
        cnt += 1
    if y >= 10 :
        cnt += 1
    if z >= 10 :
        cnt += 1

    if cnt == 0 :
        print("zilch")
    elif cnt == 1 :
        print("double")
    elif cnt == 2 :
        print("double-double")
    else :
        print("triple-double")
    print()