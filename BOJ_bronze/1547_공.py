t = int(input())
arr = [0,1,0,0]
for tc in range(t):
    a, b = map(int,input().split())
    arr[a] , arr[b] = arr[b] , arr[a]

for i in range(len(arr)):
    if arr[i] == 1:
        print(i)

# print(arr.index(1))