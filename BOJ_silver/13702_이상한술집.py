def check(x):
    total = 0

    for i in arr:
        total += i // x

    return total >= k

n , k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

s = 0
e = 100000000000

while s <= e :
    mid = (s+e) // 2

    if check(mid):
        ans = mid
        s = mid + 1
    else :
        e = mid - 1

print(ans)