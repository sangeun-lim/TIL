n, m = map(int,input().split())
arr = list(map(int,input().split()))

def recur(cur, total):
    if cur == n:
        return total == m

    return recur(cur + 1, total + arr[cur]) + recur(cur + 1, total)

print(recur(0,0) - (m == 0))