x = input()
total = 0
cnt = 0
for i in range(len(x)):
    if cnt == 0 :
        total += 10
        cnt += 1
        continue
    else :
        if x[i] == x[i-1]:
            total += 5
            continue
        else:
            total += 10
            continue
print(total)

