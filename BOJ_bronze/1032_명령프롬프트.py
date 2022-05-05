n = int(input())
if n == 1:
    print(input())
else:
    arr = [] # 입력받을 명령어들
    for tc in range(n):
        arr.append(input())

    res = list(arr[0]) # 첫번째 명령어를 기초로 잡기

    for i in range(n):
        for j in range(len(res)):
            if res[j] == arr[i][j]:
                continue
            else:
                res[j] ='?'
    print(''.join(res))
