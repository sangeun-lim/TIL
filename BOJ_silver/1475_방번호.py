N = input()
dic = {'0': 0, '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for i in N :
    if i =='6' or i=='9':
        dic['6'] += 1
    else:
        dic[i] += 1
if dic['6'] % 2 == 0 :
    dic['6'] = dic['6'] // 2
else:
    dic['6'] = dic['6'] // 2 + 1
print(max(dic.values()))

############################
number=input()
each_num=[]
count=[0]*10
for ch in number:
    each_num.append(ch)
for num in each_num:
    count[int(num)]+=1
count[6]=(count[6]+count[9]+1)//2
count[9]=count[6]
print(int(max(count)))