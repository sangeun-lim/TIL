# 내 풀이
T = int(input())
for tc in range(T):
    h, w, n = map(int,input().split())

    if n % h != 0 : # 층
        a = n % h
        a = str(a)
    else :
        a = str(h)

    b = n // h + 1  # 호수
    if n % h != 0 :
        if b < 10 :
            b = str(b)
            b = '0'+b
        else :
            b = str(b)
    else :
        b -= 1
        if b < 10 :
            b = str(b)
            b = '0' + b
        else :
            b = str(b)

    print(a+b)

#########################################
# 다른 사람 풀이
import math
T=int(input())

for t in range(T):
    h, w, n = map(int, input().split())
    if n%h == 0:
        hh = h
    else:
        hh = n%h
    ww = math.ceil(n/h)
    print(f"{hh*100+ww}")