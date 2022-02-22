T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[1] * i for i in range(1, N + 1)]
    # print(arr)
    for i in range(2, N):
        for j in range(1, i):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(f'#{tc}')
    for i in arr:
        print(' '.join(map(str, i)))

#######################################################
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    li = [0,1,0]

    print(f'#{tc}')

    while len(li) < N+3 :
        print(' '.join(list(map(str,li[1:-1]))))
        newli = [0]
        for i in range(len(li)-1):
            newli.append(li[i] + li[i+1])
        newli.append(0)
        li = newli