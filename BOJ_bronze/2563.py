T = int(input())  # 색종이의 수
square = [[0 for _ in range(100)] for _ in range(100)]  # 100x100 도화지

for tc in range(T):
    # n =색종이의 왼쪽 변과 도화지의 왼쪽 변의 거리
    # m =색종이의 아래쪽 변과 도화지의 아래쪽 변의 거리
    n,m = map(int,input().split())

    for i in range(n,n+10):
        for j in range(m,m+10):
            square[i][j] = 1

total = 0
for i in range(100):
    for j in range(100):
        total += square[i][j]

print(total)

