import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
k = int(input())

new_num = []

cnt = 0  # 쌍의 개수를 셀 변수
temp = 0 # 리스트에 합 저장할 변수

for i in num:
    temp += i
    new_num.append(temp)

for i in range(n-1,-1,-1):
    j = 0
    if new_num[i] > k:
        cnt += 1
    while new_num[i]-new_num[j] > k:
        cnt += 1
        j += 1
print(cnt)
