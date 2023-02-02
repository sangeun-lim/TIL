# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
E,S,M = map(int,input().split())
a = b = c = 1
cnt = 1
while not (E == a and S == b and M == c):
    a += 1
    b += 1
    c += 1
    if a == 16 :
        a = 1
    if b == 29 :
        b = 1
    if c == 20 :
        c = 1
    cnt += 1
print(cnt)


#############################################
import sys
input = sys.stdin.readline
e,s,m = map(int, input().split())
year = 1
while True:
    if (year -e) % 15 == 0 and (year-s) % 28 == 0 and (year-m) % 19 == 0:
        break
    year += 1

print(year)