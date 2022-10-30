N = int(input())
s = 1
e = 1
cnt = 0
total = 1

# 연속된 자연수이므로 리스트에 저장한 값을 가져올 필요가 없음
while e < N :
    if total == N :
        cnt += 1
        e += 1
        total += e
    elif total < N:
        e += 1
        total += e
    else:
        total -= s
        s += 1
print(cnt+1) # 자기 자신 포함