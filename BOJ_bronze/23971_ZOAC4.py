import math

H,W,N,M = map(int,input().split())
x = math.ceil(H / (N+1))
y = math.ceil(W / (M+1))
print(x*y)

#########################
H,W,N,M = map(int,input().split())
x = (H-1) // (N+1)
y = (W-1) // (M+1)
print((x+1)*(y+1))