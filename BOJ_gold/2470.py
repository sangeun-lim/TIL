T = int(input())                             # 전체 용액의 수
N_list = list(map(int,input().split()))      # 용액의 특성값을 나타내는 N개의 정수가 오름차순으로 입력
N_list.sort()
s = 0
e = T-1

x = N_list[0]
y = N_list[T-1]

while s < e :
    if abs(x+y) > abs(N_list[s] + N_list[e]) :
        x = N_list[s]
        y = N_list[e]
    if N_list[s] + N_list[e] < 0:
        s += 1
    else :
        e -= 1

print(x,y)