import sys
sys.stdin = open('sample_input.txt')

# T = int(input()) # 테스트 케이스 개수
#
# for tc in range(1,T+1):
#     A,B = map(str,input().split())
#     cnt = 0
#     a = len(A)
#     b = len(B)
#
#     for i in range(a-b+1):
#         if B in A :
#             cnt += 1
#             A = A.replace(B,"!")
#
#     print(f'#{tc} {len(A)}')

#############################################

T = int(input()) # 테스트 케이스 개수
for tc in range(1, T + 1):
    A, B = input().split()
    A = A.replace(B,"!")            # A에 들어있는 B 를 전부 '!' 로 치환
    print(f'#{tc} {len(A)}')
