n = int(input())
for i in range(n):
    lst = list(map(int,input().split()))
    lst.sort()
    if (lst[0] ** 2 + lst[1] **2 == lst[2] **2):
        print(f'Scenario #{i+1}:')
        print('yes')
    else:
        print(f'Scenario #{i+1}:')
        print('no')
    print()