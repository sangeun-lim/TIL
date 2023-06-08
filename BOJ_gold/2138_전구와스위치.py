n = int(input())
arr = list(map(int,input()))
target = list(map(int,input()))

def click(A,B):
    newArr = A[:]
    cnt = 0
    for i in range(1, n):
        # 이전 전구가 같은 상태면 continue
        if newArr[i-1] == B[i-1]:
            continue
        # 다른 상태면
        cnt += 1

        for j in range(i-1, i+2): # i-1~ i+1까지의 세개의 전구 상태 변환
            if j < n:
                newArr[j] = 1 - newArr[j]

    if newArr == B:
        return cnt
    else:
        return 1000000000

# 첫번째 전구를 누르지 않은 경우
res = click(arr, target)

# 첫번째 전구를 누른 경우
arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]

res = min(res, click(arr, target) + 1)
print(res if res !=1000000000 else -1)