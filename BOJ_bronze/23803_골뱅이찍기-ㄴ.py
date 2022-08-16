import sys
input = sys.stdin.readline

N = int(input())

for i in range(N*5):
    if i < (5 * N) - N :
        for j in range(N):
            print("@", end="")

    if i >= (5*N) - N :
        for j in range(N*5):
            print("@", end="")

    print()