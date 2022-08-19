import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    x = input()
    N = int(input())
    total = 0
    for i in range(N):
        total += int(input())
    if total % N == 0 :
        print('YES')
    else:
        print('NO')