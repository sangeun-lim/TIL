# n이 1000제한이므로
# 4중 포문으로 하면 시간초과
# 2중 포문을 2개로 묶는 형태로 아이디어 내기

T = int(input())
for tc in range(T):
    k, n = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(4)]

    a = []
    b = []
    for i in range(n):
        for j in range(n):
            a.append(arr[0][i] + arr[1][j])
            b.append(arr[2][i] + arr[3][j])

    a.sort()
    b.sort()

    s = 0
    e = len(b) - 1
    ans = a[s] + b[e]
    while s < len(a) and e >= 0: # s가 끝까지 가고 e가 처음까지 올때까지
        if abs(ans - k) > abs(a[s] + b[e] - k):
            ans = a[s] + b[e]
        elif abs(ans - k) == abs(a[s] + b[e] - k): # 조건에 근사값이 같을 때 더 작은값을 선택한다는 말이 있었음
            ans = min(ans, a[s] + b[e])

        if a[s] + b[e] > k:
            e -= 1
        elif a[s] + b[e] < k:
            s += 1
        else:
            break
    print(ans)