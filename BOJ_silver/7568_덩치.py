N = int(input())
person = [list(map(int,input().split())) for _ in range(N)]
ans = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i, end=" ")