# True들 중에서 가장 왼쪽 인덱스의 값과 개수 구하기
# xxxxxoooooo 형태임
import sys
input = sys.stdin.readline

def check(x): # x이하의 정수의 개수가 홀수개인지 체크 , 왜냐하면 홀수를 true로 했을때 가장 왼쪽 인덱스를 찾아야함
    cnt = 0
    for a, c, b in arr:
        minX = min(c,x)
        if a <= x:
            cnt += ((minX-a) // b) + 1
        # if a <= x:
        #     cnt += min((c - a), (x - a)) // b + 1
    return cnt % 2

def countNum(x):
    cnt = 0
    for a, c, b in arr:
        if x < a or x > c:
            continue
        if (x-a) % b == 0:
            cnt += 1

    return cnt

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = -1
s = 1
e = 2147483647

while s <= e :
    mid = (s+e) // 2
    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

if ans == -1:
    print('NOTHING')
else:
    print(ans, countNum(ans))

#----------------------------------------------------------#
import sys
input = sys.stdin.readline

def check(x): # x이하의 정수의 개수가 홀수개인지 체크 , 왜냐하면 홀수를 true로 했을때 가장 왼쪽 인덱스를 찾아야함
    cnt = 0
    for a, c, b in arr:
        minX = min(c,x)
        if a <= x:
            cnt += ((minX-a) // b) + 1
        # if a <= x:
        #     cnt += min((c - a), (x - a)) // b + 1
    return cnt

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = -1
s = 1
e = 2147483647

while s <= e :
    mid = (s+e) // 2
    if check(mid) % 2:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

if ans == -1:
    print('NOTHING')
else:
    print(ans, check(ans) - check(ans-1))