A = int(input()) # 원래의 고기 온도
B = int(input()) # 목표 온도
C = int(input()) # 얼어있는 고기를 섭씨1도 올리는데 걸리는 시간
D = int(input()) # 고기를 해동하는데 걸리는 시간
E = int(input()) # 얼어 있찌 않는 고기를 섭씨 1도 올리는데 걸리는 시간

cnt = 0
if A < 0 :
    cnt += abs(A) * C + D + B * E
elif A == 0 :
    cnt += D + B*E
else :
    cnt += (B-A) * E

print(cnt)