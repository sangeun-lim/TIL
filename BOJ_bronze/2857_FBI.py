name = []
for i in range(5):
    x = input()
    name.append(x)
cnt = 0
cnt_list = []
for i in name:
    cnt += 1
    if 'FBI' in i :
        cnt_list.append(cnt)
if cnt_list :
    print(*cnt_list)
else:
    print('HE GOT AWAY!')