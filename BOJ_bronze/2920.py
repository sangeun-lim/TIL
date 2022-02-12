sounds = list(map(int,input().split()))

asc = []
desc = []

for i in range(len(sounds)) :
    if int(i+1) == sounds[i]:
        asc.append(i+1)
    elif int(8-i) == sounds[i]:
        desc.append(8-i)
    else:
        continue

if sounds == asc :
    print('ascending')
elif sounds == desc :
    print('descending')
else :
    print('mixed')
