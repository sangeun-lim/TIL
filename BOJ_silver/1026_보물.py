n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort()
arr2 = arr2[::-1]
x = 0
total = 0
for i in arr1 :
    total += i * arr2[x]
    x += 1
print(total)