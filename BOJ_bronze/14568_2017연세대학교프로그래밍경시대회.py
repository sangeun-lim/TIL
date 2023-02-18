# N = 6 : 1
# N = 7 : 1
# N = 8 : 3 => 1 + 2
# N = 9 : 3 => 1 + 2
# N = 10 : 6 => 1 + 2 + 3
# N = 11 : 6 => 1 + 2 + 3
# N = 12 : 10 => 1 + 2 + 3 + 4
N = int(input())
if N < 6:
    print(0)
else:
    N = N - 6
    x = N // 2
    cnt = 0
    for i in range(1,x+2):
        cnt += i
    print(cnt)
#-------------------------------#
N = int(input())
cnt = 0
for i in range(2, N - 1, 2):
    cnt += (N - i - 2) //2
print(cnt)