import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1,T+1):
    test, N = map(str,input().split())
    N = int(N)
    num_list = list(map(str,input().split()))

    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    sort_num = []

    for i in range(len(num)):
        for n in num_list:
            if num[i] == n :
                sort_num.append(num[i])

    print(f'{test}' ,end=' ')
    for i in range(N):
        print(sort_num[i], end=' ')
    print()
#######################################
    # print(f'{test}' ,end=' ')
    # print(' '.join(sort_num))
####################################
    # print(*sort_num)