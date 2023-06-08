# 카운팅 배열 사용
n = int(input())
arr = [int(input()) for i in range(n)]
cnt = [0 for i in range(110)]
ans = 0
if n > 1:
    for i in arr[1:]:
        cnt[i] += 1

    idx = max(arr[1:]) # 1번 기호 빼고 가장 큰 득표수
    cur = arr[0] #다솜이 득표수
    ans = 0

    while cur <= idx:
        cur += 1
        ans += 1

        cnt[idx] -= 1
        cnt[idx-1] += 1

        if cnt[idx] == 0:
            idx -= 1
print(ans)