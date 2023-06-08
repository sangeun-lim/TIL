n, m = map(int,input().split())
arr = list(map(int,input().split()))
v = [[] for i in range(2)]

def recur(cur, total, idx, end):
    if cur == end:
        v[idx].append(total)
        return

    recur(cur + 1, total + arr[cur], idx, end)
    recur(cur + 1, total, idx, end)

recur(0, 0, 0, n//2)
recur(n//2, 0, 1, n)
# v[0].remove(0)
# v[1].remove(0)

v[0].sort()
v[1].sort()

s = 0
e = len(v[1]) - 1
cnt = 0

while s < len(v[0]) and e >= 0:
    if v[0][s] + v[1][e] == m:
        temp = v[0][s]
        x = 0
        while s < len(v[0]) and v[0][s] == temp:
            x += 1
            s += 1

        temp = v[1][e]
        y = 0
        while e >= 0 and v[1][e] == temp:
            y += 1
            e -= 1

        cnt += x * y
    elif v[0][s] + v[1][e] > m:
        e -= 1
    else:
        s += 1

if m == 0:
    cnt -= 1

print(cnt)