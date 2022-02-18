import sys
sys.stdin = open('sample_input.txt')

T = int(input()) # 테스트 케이스 개수

for tc in range(1,T+1):
    p = input()     # 찾을 패턴
    t = input()     # 전체 텍스트

    M = len(p)      # 찾을 패턴의 길이
    N = len(t)      # 전체 텍스트의 길이

    i = 0           # t의 인덱스
    j = 0           # p의 인덱스

    ans = 0         # 출력에 쓰일 변수

    # 찾을 패턴의 인덱스가 찾을 패턴의 길이보다 작고,
    # 전체 텍스트의 인덱스가 전체 텍스트의 길이보다 작으면
    while j < M and i < N :
        # 문자열이 각각 일치하지 않는다면
        if t[i] != p[j] :
            i = i - j      # 찾을 패턴의 처음으로
            j = -1         # 패턴의 인덱스를 -1
        i = i + 1          # 다음 인덱스 확인
        j = j + 1          # 다음 패턴의 인덱스 확인
    # 패턴의 길이와 패턴의 인덱스값이 같다면
    if j == M :
        ans = 1
    else :
        ans = 0

    print(f'#{tc} {ans}')

# ####################################################

T = int(input()) # 테스트 케이스 개수
for tc in range(1,T+1):
    p = input()     # 찾을 패턴
    t = input()     # 전체 텍스트

    M = len(p)      # 찾을 패턴의 길이
    N = len(t)      # 전체 텍스트의 길이

    ans = 0

    for i in range(N-M+1):
        if t[i:i+M] == p:
            ans = 1

    print(f'#{tc} {ans}')

###########################################
T = int(input())

def brute_force(pattern, text):
    i = j = 0

    p = len(pattern)
    t = len(text)

    while j < p and i < t:
        if pattern[j] != text[i]:
            i -= j
            j = -1
        i += 1
        j += 1

    # if j == p :
    #     return 1
    # else :
    #     return 0
    return 1 if j == p else 0


for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    result = brute_force(str1,str2)
    print(f'#{tc} {result}')