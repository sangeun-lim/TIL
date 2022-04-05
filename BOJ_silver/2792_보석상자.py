import sys

def check(x):
    total = 0

    for i in arr:
        if i % x == 0 :
            total += i // x
        else :
            total += i // x + 1
        # total += i // x + (i % x != 0)
    return total <= n

n , m = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(m)]

s = 1
e = 10000000000

while s <= e :
    mid = (s + e) // 2

    if check(mid):
        ans = mid
        e = mid - 1
    else :
        s = mid + 1

print(ans)