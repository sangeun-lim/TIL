n = int(input())
for i in range(n):
    a1,p1 = map(int,input().split())
    r1,p2 = map(int,input().split())
    whole = r1 * r1 * 3.14 / p2
    slice = a1 / p1
    if whole > slice :
        print('Whole pizza')
    else :
        print('Slice of pizza')