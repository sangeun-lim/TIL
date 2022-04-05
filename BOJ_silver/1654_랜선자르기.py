def check(x): # 잘라진 길이들 입력받기
    total = 0

    for i in arr:
        total += i // x

    return total >= m

n, m = map(int,input().split())
arr = [int(input()) for i in range(n)]

s = 1
e = 100000000000

while s <= e :
    mid = (s+e) // 2

    if check(mid):
        ans = mid
        s = mid + 1
    else :
        e = mid - 1

print(ans)