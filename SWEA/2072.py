T = int(input())

for tc in range(1,T+1):
    test_list = list(map(int,input().split()))
    total = 0

    for i in range(len(test_list)):
        if test_list[i] % 2 == 1:
            total += test_list[i]

    print(f'#{tc} {total}')