T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    print(min(lst), max(lst))