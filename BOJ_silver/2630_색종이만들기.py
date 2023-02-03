def recur(x,y,size):
    start = square[x][y]
    same = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            if square[i][j] != start:
                same = False
                break
    if same:
        result[start] += 1
    else:
        size //= 2
        for i in range(2):
            for j in range(2):
                recur(x + size * i, y + size * j, size)

N= int(input())
square = [list(map(int,input().split())) for _ in range(N)]
result = [0,0]
recur(0,0,N)
print(result[0])
print(result[1])

