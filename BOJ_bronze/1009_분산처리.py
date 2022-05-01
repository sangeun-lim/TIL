"""
1 : 1
2 : 2,4,8,6
3 : 3,9,7,1
4 : 4,6
5 : 5
6 : 6
7 : 7,9,3,1
8 : 8,4,2,6
9 : 9,1
0 : 10
"""

T = int(input())
for tc in range(T):
    a, b = map(int,input().split())
    a = a % 10 # a의 1의 자리수 초기화

    if a == 0 : # a의 1의 자리수가 0이면
        print(10)
    elif a == 1 or a == 5 or a == 6 : # a의 1의 자리수가 1 또는 5 또는 6이면
        print(a)
    elif a == 4 or a == 9: # a의 1의 자리수가 4 또는 9 이면
        b = b % 2 # 4,6 일때와 9,1 일때를 나누기 위해
        if b : # b 가 짝수면
            print(a)
        else : # b 가 홀수면
            print(a ** 2 % 10)
    else : # a의 1의 자리수가 2 ,3 , 7 ,8 이면
        b = b % 4 # b 제곱한 수의 1의 자리수가 4가지 경우가 있으므로
        if b == 0 :
            print(a ** 4 % 10)
        else :
            print(a ** b % 10)
