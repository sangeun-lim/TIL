N = int(input())
arr = [0] * 1001
if N < 100 :
    arr[N] = N
else :
    cnt = 99
    for i in range(100,1001):
        i = str(i)
        if int(i[0])-int(i[1]) == int(i[1]) -int(i[2]): # 등차수열일때
            cnt += 1
        i = int(i)
        arr[i] = cnt
print(arr[N])
