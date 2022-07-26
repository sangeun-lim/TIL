from itertools import combinations

N,M = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
total = 0

# 전체 m종류의 치킨중 3개를 고르는 조합
for a,b,c in combinations(range(M),3):
    temp = 0
    for i in range(N):
        temp += max(lst[i][a], lst[i][b], lst[i][c])
    total = max(total, temp)
print(total)