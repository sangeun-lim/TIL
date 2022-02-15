T = int(input())

for tc in range(1,T+1):
    test_list = list(map(int,input().split()))
    total = 0

    for i in range(len(test_list)):
        total += test_list[i]

    total = total / len(test_list)

    print(f'#{tc} {round(total)}')