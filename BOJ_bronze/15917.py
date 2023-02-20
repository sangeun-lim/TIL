import sys
input = sys.stdin.readline

Q = int(input())
for i in range(Q):
    a = int(input())
    if a == 1 :
        print(1)
    else:
        while True:
            if a % 2 == 0:
                pass
            else:
                if a == 1:
                    print(1)
                    break
                else:
                    print(0)
                    break
            a //= 2
#-------------------------------#
import sys
input=sys.stdin.readline
for i in range(int(input())):
    a=int(input())
    print(+((a&(-a)) == a))