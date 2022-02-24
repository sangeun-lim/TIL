# n,k = map(int,input().split()) # n 은 학생수 , k 는 한방의 최대 인원 수
#
# room = 0
# stu = []
#
# for i in range(n):
#     s,y = map(int,input().split()) # s는 성별 , y 는 학년
#     stu.append((s,y))
#
# stu_cnt = [0] * 13
#
# for i in stu :
#     if i[0] == 1 : # 남자일때
#         for j in range(1,7):
#             if i[1] == j:
#                 stu_cnt[j] += 1
#     else :         # 여자일때
#         for j in range(1,7):
#             if i[1] == j:
#                 stu_cnt[j+6] += 1
# for i in stu_cnt:
#     if i % 2 == 0 :
#         room += i//2
#     else :
#         room += i//2 + 1
#
# print(room)

########################################################
n,k = map(int,input().split()) # n 은 학생수 , k 는 한방의 최대 인원 수
stu = [[0]*2 for _ in range(6)] # 성별 2개, 학년 6개

for i in range(n):
    s, y = map(int, input().split())
    stu[y-1][s] += 1
# print(stu)
room = 0
for i in range(6): # 학년별
    for j in range(2): # 성별
        if (stu[i][j] % k) == 0 : # 학생수가 k로 나누어 떨어지면
            room += stu[i][j]//k
        else:
            room += stu[i][j]//k + 1
print(room)