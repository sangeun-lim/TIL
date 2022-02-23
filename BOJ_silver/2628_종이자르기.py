row, col = map(int,input().split())            # 가로 , 세로 길이 받기
cut = int(input())                             # 자르는 횟수

my_paper_row = [0,row]
my_paper_col = [0,col]

# 자를 위치값 넣어주기
for i in range(cut):
    num, down_right = map(int,input().split())
    if num == 0 :
        my_paper_col.append(down_right)
    else :
        my_paper_row.append(down_right)

# 리스트 정렬
for i in range(len(my_paper_row)-1, 0, -1):
    for j in range(i):
        if my_paper_row[j]>my_paper_row[j+1]:
            my_paper_row[j],my_paper_row[j+1] =  my_paper_row[j+1] , my_paper_row[j]

for i in range(len(my_paper_col)-1, 0, -1):
    for j in range(i):
        if my_paper_col[j]>my_paper_col[j+1]:
            my_paper_col[j],my_paper_col[j+1] =  my_paper_col[j+1] , my_paper_col[j]

# my_paper_col.sort()
# my_paper_row.sort()

max_row = 0
max_col = 0

# 정렬된 값들을 앞에서부터 순차적으로 2개씩 묶어서 가장 큰 수들만 추려낸다.
for i in range(len(my_paper_row)-1):
    if my_paper_row[i+1] - my_paper_row[i] > max_row:
        max_row = my_paper_row[i+1] - my_paper_row[i]

for i in range(len(my_paper_col)-1):
    if my_paper_col[i+1] - my_paper_col[i] > max_col:
        max_col = my_paper_col[i+1] - my_paper_col[i]

# 추려낸 값들 중 가장 큰 값끼리 곱함
big_paper = max_row * max_col

print(big_paper)
