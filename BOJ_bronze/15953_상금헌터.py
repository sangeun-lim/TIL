T = int(input())
lst1=[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6
lst2=[512]+[256]*2+[128]*4+[64]*8+[32]*16
for i in range(T):
    total = 0
    a,b = map(int,input().split())
    a = a-1
    b = b-1
    if a != -1 and a < 21:
        total += lst1[a] * 10000
    if b != -1 and b < 31:
        total += lst2[b] * 10000
    print(total)