n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
visited = [[False for j in range(3 * n)] for k in range(2)]
ans = 0

def recur(x,y, cnt):
    global ans

    if n % 2: # 홀수일때
        if y == n:
            x += 1
            y = 0
        elif y == n+1: # 2칸씩 넘어가니까 범위를 벗어날수도잇음
            x += 1
            y = 1
    else:     # 짝수일때
        if y == n:
            x += 1
            y = 1
        elif y == n+1:
            x += 1
            y = 0

    if x == n:
        ans = max(ans, cnt)
        return

    # x+y => 행과 열의 합이 같은경우 비숍이 못감
    # x-y => 마찬가지
    if arr[x][y] == 1 and not visited[0][x+y] and not visited[1][x-y]:
        visited[0][x+y] = True
        visited[1][x-y] = True
        recur(x, y + 2, cnt + 1)
        visited[0][x+y] = False
        visited[1][x-y] = False

    recur(x, y+ 2, cnt)

ans = 0
recur(0,0,0)
Black = ans

ans = 0
recur(0,1,0)
White = ans

print(Black + White)