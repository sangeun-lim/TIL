k = int(input())

word = ['A','B']
a_cnt = 0
b_cnt = 0
for i in range(2,k+1):
    word.append(word[i-1]+word[i-2])

if k == 1:
    b_cnt = 1
elif k == 2 :
    a_cnt = 1
    b_cnt = 1
else :
    for i in word[-1]:
        if i == 'A' :
            a_cnt += 1
        else :
            b_cnt += 1

print(f'{a_cnt} {b_cnt}')

#########################################
k = int(input())

word = [0] * (k+1)
word[1] = 1

for i in range(2,k+1):
    word[i] = word[i-2] + word[i-1]

print(word[-2], word[-1])