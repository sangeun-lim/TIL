# 오른쪽의 가장 큰 인덱스를 찾는 문제
# 거리     1 2 3 4 5 6 7 8 9
# 가능여부 o o o x x x x x x
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
arr = sorted([int(input()) for i in range(n)])

def check(x):
    cnt = c - 1   # 공유기 처음 한개 사용 (공유기 개수)
    now =  arr[0] # 첫 공유기 초기 위치값
    for i in range(1,n):
        if arr[i] - now >= x: # x거리 이상 떨어졌는지 확인
            cnt -= 1
            if cnt == 0: # 공유기를 다 설치했으면
                return True
            now = arr[i] # 공유기 설치 위치 갱신

    return False

ans = 0
s = 1
e = arr[n-1] - arr[0]

while s <= e:
    mid = (s+e) // 2
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
