x,y,z = map(int,input().split())
sum1 = {}
for i in range(1,x+1):
    for j in range(1,y+1):
        for k in range(1,z+1):
            total = i+j+k
            if total in sum1 :
                sum1[total] += 1
            else :
                sum1[total] = 1
res = sorted(sum1.items(), key=lambda x:x[0])
res = sorted(res, key=lambda x:x[1], reverse=True)
print(res[0][0])

#####################################################
s1, s2, s3 = map(int, input().split())
li = [0]*81
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            li[i+j+k] += 1
print(li.index(max(li)))