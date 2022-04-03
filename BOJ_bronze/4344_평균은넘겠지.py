C = int(input())
for tc in range(C):
    N , *arr = map(int,input().split())
    avg = sum(arr)/N
    cnt = 0
    for i in range(N):
        if arr[i] > avg:
            cnt += 1
    percent = cnt / N * 100

    print(f'{percent:.3f}%')

##########################################
word = input()
dial = [0, 0, 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV','WXYZ']
result = 0
for i in word:
    for j in range(2, 10):
        if i in dial[j]:
            result += j+1
print(result)