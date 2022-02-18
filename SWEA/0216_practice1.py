import sys
sys.stdin = open('practice1\input.txt')

T = int(input())

for tc in range(1,T+1):
    s = input()
    print(f'#{tc} {s[::-1]}')