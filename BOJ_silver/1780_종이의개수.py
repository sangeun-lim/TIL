def recur(x, y, size):
    start = arr[x][y] # 현재 종이의 시작 부분의 숫자값 기억
    same = True
    for i in range(x, x + size):
        for j in range(y, y+size):
            if arr[i][j] != start:
                same = False
                break
    if same:
        result[start] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                recur(x + size * i, y + size * j, size)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = {-1:0, 0:0, 1:0}
recur(0,0,n)
print(result[-1])
print(result[0])
print(result[1])

###########################################################################

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

minus = 0
zero = 0
plus = 0

def recur(x, y, size):
    global minus, zero, plus

    start = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != start:
                for k in range(3):
                    for l in range(3):
                        recur(x + k * size // 3, y + l * size // 3, size // 3)
                return

    if start == -1 :
        minus += 1
    elif start == 0 :
        zero += 1
    else :
        plus += 1

recur(0,0,n)
print(minus)
print(zero)
print(plus)