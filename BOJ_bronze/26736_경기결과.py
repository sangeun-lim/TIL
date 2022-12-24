X = input()
A_cnt = 0
B_cnt = 0
for i in X:
    if i == 'A':
        A_cnt += 1
    else :
        B_cnt += 1
print(f'{A_cnt} : {B_cnt}')