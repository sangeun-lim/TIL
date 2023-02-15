N, X, K = map(int,input().split())
lst = [0] * (N+1)
lst[X] = 1
for i in range(K):
    A,B = map(int,input().split())
    lst[A],lst[B] = lst[B],lst[A]

print(lst.index(1))

#-----------------------------------------#
import sys
input = sys.stdin.readline

n, x, k = map(int, input().split())
for i in range(k):
  a, b = map(int, input().split())
  if a == x:
    x = b
  elif b == x:
    x = a
print(x)