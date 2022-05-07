import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    A, B = map(int, input().split())

    if A % B == 0 or B % A == 0:
        print(max(A,B))
    else:
        if A < B :
            A,B = B,A

        C,D = A,B
        while True:
            r = C % D
            C = D
            D = r

            if r == 0 :
                break
        print(A*B//C)

######################

import math

T = int(input())
for tc in range(T):
    a,b = map(int,input().split())
    print(math.lcm(a,b))