n = int(input()) # 터널을 조사한 시간
m = int(input()) # 터널 안에 들어있는 차량의 수
max_Car = m
for i in range(n):
    x, y = map(int,input().split()) # 입구 통과한 차와 출구를 통과한 차
    m += x
    m -= y
    max_Car = max(m,max_Car)
    if m < 0:
        print(0)
        break
else:
    print(max_Car)