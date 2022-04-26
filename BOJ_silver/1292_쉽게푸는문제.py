A,B = map(int,input().split())
arr = [0]
for i in range (1, B+1):
    for j in range(1,i+1):
        arr.append(i)
total = 0
for i in range(A,B+1):
    total += arr[i]

print(total)