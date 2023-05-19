import sys
input = sys.stdin.readline
N = int(input())
lst1 = list(map(int,input().split()))
M = int(input())
lst2 = list(map(int,input().split()))

dict = {}
for i in range(len(lst1)):
    dict[lst1[i]] = 0

for i in lst2:
    if i in dict.keys():
        print(1, end=" ")
    else:
        print(0, end=" ")


############################
import sys

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')

##################################
import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
ref = list(map(int, sys.stdin.readline().split()))

ans = []
for r in ref:
    if r in cards:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)

#--------------------------------------#
n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    ans = 0

    s = 0
    e = n-1
    while s <= e:
        mid = (s+e) // 2

        if arr[mid] == i:
            ans = 1
            break
        elif arr[mid] < i:
            s = mid + 1
        else:
            e = mid - 1

    print(ans, end=' ')