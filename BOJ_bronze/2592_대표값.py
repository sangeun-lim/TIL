total = 0
dic = {}
for i in range(10):
    x = int(input())
    total += x
    if x in dic :
        dic[x] += 1
    else:
        dic[x] = 1

avg = total // 10
res = sorted(dic.items(), key=lambda x:x[1], reverse=True)
print(avg)
print(res[0][0])
