import sys
sys.stdin = open('input.txt')

xy = [[0] * 100 for i in range(100)]

for tc in range(4):
    square = list(map(int, input().split()))
    for i in range(square[0],square[2]):
        for j in range(square[1],square[3]):
            xy[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if xy[i][j] >= 1 :
            cnt += 1

print(cnt)
