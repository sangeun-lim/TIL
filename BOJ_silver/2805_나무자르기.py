def check(x):
    total = 0
    for i in tree:
        if i >= x :
            total += i - x
        # total += max(0, i-x)
    return total >= M

N,M = map(int,input().split()) # 나무의 수 N , 가져가려는 나무의 길이 M
tree = list(map(int,input().split()))  # 나무의 높이

s = 0
e = 10000000000
cnt = 0
while s <= e:
    mid = (s+e) // 2

    if check(mid):
        cnt = mid
        s = mid + 1
    else :
        e = mid - 1

print(cnt)