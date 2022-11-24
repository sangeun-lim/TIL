while True:
    x = int(input())
    if x == 0 :
        break
    else:
        lst = list(map(int,input().split()))
        cnt1 = lst.count(0)
        cnt2 = lst.count(1)
        print(f'Mary won {cnt1} times and John won {cnt2} times')