import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트케이스 개수
for tc in range(1,T+1):
    alpha = list(input())
    result = []

    for i in alpha:
        if result and i == result[-1]:        # result에 값이 있고, i 가 result의 마지막값과 같으면 pop
            result.pop()
        else:                                 # result에 값이 없거나, i가 result의 마지막값과 같지 않으면 append
            result.append(i)

    print(f'#{tc} {len(result)}')











#####################################
#
# T = int(input())
# for tc in range(1,T+1):
#     alpha = list(input())
#     result = []
#
#     while alpha:
#         s = alpha.pop(0)
#         if not result or result[-1] != s:
#             result.append(s)
#         else:
#             result.pop()
#
#     print(f'#{tc} {len(result)}')