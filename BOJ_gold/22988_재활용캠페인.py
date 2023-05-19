# 1. 이미 x 이상인 것은 제외
# 2. 투포인터로 두개씩 묶어서 제작
# 3. (남은 것들 // 3) 이 추가

n,x = map(int,input().split())
arr = sorted(list(map(int,input().split())))

bottle = n # 남은 용기 개수
cnt = 0 # 꽉 찬 헤어에센스 용기 개수
s = 0
e = n -1

for i in range(n)[::-1]:
    if arr[i] == x: # x 이상인 것 제외
        cnt += 1
        e = i - 1
        bottle -= 1

while s < e:
    # if (arr[s] + arr[e] >= x / 2: # 아래 코드가 더 안정적
    if 2 * (arr[s] + arr[e]) >= x:
        cnt += 1
        bottle -= 2
        e -= 1
    s += 1

print(cnt + bottle // 3)