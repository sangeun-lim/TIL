lst = list(map(int,input().split()))
for i in lst :
    if i == 0 or i == 1 :
        pass
    else:
        print('F')
        exit()
print('S')