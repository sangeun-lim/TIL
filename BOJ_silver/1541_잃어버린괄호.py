problem = input()
res = 0 # 이 식의 최소값(결과값)
change_str = '' # 숫자로 변환시켜줄 문자
minus = False # '-' 기호 판별 여부를 위한 변수

for i in problem:
    if i in '-+':
        if minus:
            res -= int(change_str)
        else :
            res += int(change_str)
        change_str = ''
    else:
        change_str += i
    if i == '-':
        minus = True
else:
    if minus:
        res -= int(change_str)
    else:
        res += int(change_str)

print(res)

##########################################
st = input()

ls = list(st.split('-'))
sum_ls = 0

for i in range(0, len(ls)):
    if '+' in ls[i]:
        ls_pl = list(map(int, ls[i].split('+')))
        if i == 0:
            sum_ls += sum(ls_pl)
        else:
            sum_ls -= sum(ls_pl)
    else:
        if i == 0:
            sum_ls += int(ls[i])
        else:
            sum_ls -= int(ls[i])

print(sum_ls)