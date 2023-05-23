def get_cloud():
    global cloud

    cloud = [] # 클라우드 비우기
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                cloud.append([i,j])

def get_exist(): # 구름의 위치를 나타내는 2차원 배열
    global exist

    exist = [[False for i in range(n)] for j in range(n)]
    for i in range(len(cloud)):
        exist[cloud[i][0]][cloud[i][1]] = True

def move(dir, dist):
    for i in range(len(cloud)):
        x,y = cloud[i][0], cloud[i][1]

        x = (x + dist * dx[dir] + 100 * n) % n
        y = (y + dist * dy[dir] + 100 * n) % n

        cloud[i][0] = x
        cloud[i][1] = y

    get_exist()

def rain():
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                arr[i][j] += 1

    # 둘 중 아무거나 써도 됨
    # for i in range(len(cloud)):
    #     arr[cloud[i][0][cloud[i][1]]] += 1

def water():
    arr2 = []
    for i in range(n):
        arr2.append(arr[i].copy())

    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                for k in range(4):
                    nx = i + dx2[k]
                    ny = j + dy2[k]

                    if 0 <= nx < n and 0 <= ny < n and arr2[nx][ny] > 0:
                        arr[i][j] += 1

def make_cloud():
    global cloud

    cloud = []
    for i in range(n):
        for j in range(n):
            if not exist[i][j] and arr[i][j] >= 2:
                arr[i][j] -= 2
                cloud.append([i,j])

    get_exist()

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)] # 패딩을 해야할지 말아야할지 고민해야함
exist = [[False for i in range(n)] for j in range(n)]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

get_exist()

# 8방향(인덱스 1부터니까 0번인덱스는 패딩)
# 왼쪽, 왼쪽위, 위, 오른쪽위, 오른쪽, 오른쪽아래, 아래, 왼쪽아래
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# 대각선
# 왼쪽위, 오른쪽위, 오른쪽아래, 왼쪽아래
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, 1, -1]

for i in range(m):
    dir, dist = map(int,input().split()) # 방향, 거리

    move(dir, dist)      # 구름 이동
    rain()               # 구름이 있는 위치에 비내리기
    water()              # 물복사
    make_cloud()         # 구름 만들기

res = 0
for i in range(n):
    for j in range(n):
        res += arr[i][j]
print(res)