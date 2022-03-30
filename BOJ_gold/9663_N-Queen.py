n = int(input())
arr = [0 for _ in range(n)]
cnt = 0

def check(cur): # 대각선이 겹치냐 안 겹치나 판단
    for i in range(cur):
        if arr[cur] == arr[i] or cur-i == abs(arr[cur]-arr[i]): # 같은 열이거나, 대각선으로 만날수있는 경우라면
            return False
    return True

def recur(cur):
    global cnt

    if cur == n : # 기저조건 , 퀸이 전부 놓인 경우
        cnt += 1
        return

    for i in range(n):
        arr[cur] = i
        if check(cur):
            recur(cur+1)

recur(0)
print(cnt)
################################################################
n = int(input())
arr = [0] * n
visited = [False for i in range(n)]
cnt = 0

def check(cur):
    for i in range(cur):
        if arr[cur] == arr[i] or cur-i == abs(arr[cur]-arr[i]): # 같은 열이거나, 대각선으로 만날수있는 경우라면
            return False
    return True

def recur(cur):
    global cnt

    if cur == n :
        cnt += 1
        return

    for i in range(n):
        if visited[i] :
            continue

        arr[cur] = i

        if check(cur):
            visited[i] = True
            recur(cur + 1)
            visited[i] = False

recur(0)
print(cnt)
#################################################################
n = int(input())
arr = [0 for _ in range(n)]
visited = [False for i in range(n)]
visited2 = [False for i in range(3 * n)]
visited3 = [False for i in range(3 * n)]
cnt = 0

def recur(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i] or visited2[cur + i] or visited3[cur - i + n]:
            continue

        visited[i] = True
        visited2[cur + i] = True
        visited3[cur - i + n] = True
        recur(cur + 1)
        visited[i] = False
        visited2[cur + i] = False
        visited3[cur - i + n] = False

recur(0)
print(cnt)

############################################
def check(cur):
    for i in range(cur):
        if arr[cur] == arr[i] or cur - i == abs(arr[cur] - arr[i]):  # 같은 열이거나, 대각선으로 만날수있는 경우라면
            return False
    return True


def recur(cur):
    global cnt

    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        arr[cur] = i

        if check(cur):
            visited[i] = True
            recur(cur + 1)
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [0] * n
    visited = [False for i in range(n)]
    cnt = 0

    recur(0)
    print(f'#{tc} {cnt}')



