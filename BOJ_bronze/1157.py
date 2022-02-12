my_alpha = input().upper()

cnt = [0 for i in range(26)]

for i in my_alpha:
    cnt[ord(i) - ord('A')] += 1

if cnt.count(max(cnt)) > 1 :        # 알파벳의 개수가 같은 값이 두개이상일 때 
    print('?')
else :
    print(chr(ord('A')+cnt.index(max(cnt))))



############################################

my_alpha = input().upper()
unique_alpha = list(set(my_alpha)) # 중복제거

# 각 알파벳이 몇번 사용되었는지 list로 저장
cnt_list = []
for i in unique_alpha :
    cnt = my_alpha.count(i)
    cnt_list.append(cnt)

# 최대값이 2개이상이면 ? 출력
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
# 최대값이 1개일때는 해당하는 알파벳 출력
else :
    idx = cnt_list.index(max(cnt_list))
    print(unique_alpha[idx])