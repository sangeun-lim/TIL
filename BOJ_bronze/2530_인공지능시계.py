a,b,c = map(int,input().split())
d = int(input())

e = a * 3600 + b * 60 + c + d
a = (e // 3600) % 24
b = (e % 3600 // 60) % 60
c = (e % 3600 % 60) % 60


print(f'{a} {b} {c}')