import sys
input = sys.stdin.readline
A,B = map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))
C = arrA + arrB
C.sort()

print(*C)