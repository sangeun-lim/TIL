R,C,N = map(int,input().split())

if R % N != 0 :
    R = R // N + 1
else :
    R = R // N

if C % N != 0 :
    C = C // N + 1
else :
    C = C // N

print(R*C)