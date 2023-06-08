# 모든 나무는 한번만 자르는게 최선
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

res = []
for i in range(n):
    res.append((arr[i],arr2[i]))
res.sort(key=lambda x:x[1])

total = 0
for i in range(n):
    total += res[i][0] + res[i][1]*i
print(total)

