N = int(input())
lst = []
for i in range(N):
    x, y = map(int,input().split())
    if x <= y :
       lst.append(y)
if len(lst) > 0:
    print(min(lst))
else:
    print(-1)