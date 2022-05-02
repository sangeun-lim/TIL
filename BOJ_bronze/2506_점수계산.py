N = int(input())
arr = list(map(int,input().split()))
score = 1
total = 0

for j in arr:
    if j == 1 :
        total += score
        score += 1
    else :
        score = 1

print(total)
