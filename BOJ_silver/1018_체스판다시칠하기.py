N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
arr2 = []

for i in range(N-7):
    for j in range(M-7):
        cnt1 = cnt2 = 0
        for x in range(i,i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if arr[x][y] != 'W':
                        cnt1 += 1
                    if arr[x][y] != 'B':
                        cnt2 += 1
                else :
                    if arr[x][y] != 'B':
                        cnt1 += 1
                    if arr[x][y] != 'W':
                        cnt2 += 1
        arr2.append(cnt1)
        arr2.append(cnt2)
print(min(arr2))