cnt = 1
while True:
    x, *lst = map(int,input().split())
    if x == 0:
        break
    else:
        if x % 2: # 홀수면
            print(f'Case {cnt}: {lst[x//2]:.1f}')
        else:
            print(f'Case {cnt}: {(lst[x//2]+lst[x//2-1])/2:.1f}')
    cnt += 1