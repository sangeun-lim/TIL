K = int(input())
D1, D2 = map(int,input().split())
h = K ** 2 - (abs(D1-D2)/2) ** 2
print(h)