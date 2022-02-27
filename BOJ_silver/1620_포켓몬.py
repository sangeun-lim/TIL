import sys
input = sys.stdin.readline

M, N = map(int,input().split()) # M은 포켓몬 이름, N은 문제 수
pocketmon = []
for i in range(M):
    tmp = input().strip()
    pocketmon.append(tmp)

for i in range(N):
    problem = input().strip()

    if problem.isdigit():
        print(pocketmon[int(problem)-1])
    else :
        print(pocketmon.index(problem)+1)
