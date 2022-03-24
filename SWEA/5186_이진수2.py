import sys
sys.stdin=open('sample_input.txt')


T = int(input())
for tc in range(1,T+1):
    n = float(input())
    ans = ''

    # 0.625 ==> 0.625 * 2 = 1.25 ==> 정수자리 도출
    # ans = '1'
    # (1.25 - 1) * 2 = 0.5 ==> 정수자리 도출
    # ans = '10'
    # 0.5 * 2 ==> 1.0 ==> 정수자리 도출
    # ans = '101'
    # 1.0 - 1 = 0.0 ==> 종료

    cnt = 0                 # 소수점 자리를 세는 변수
    # while n != 0 and cnt < 13:
    while True:             # 정답이 나오거나, overflow가 되거나
        n *= 2
        if 1 <= n < 2 :     # n에 2를 곱한 값이 1~2 사이라면 1의 자리숫자를 ans에 추가하고 n을 1 빼줌
            ans += '1'
            n -= 1
            cnt +=1         # 소수점 자리 추가
            if n == 0.0 :   # 소수점 12자리 이내 n이 0이 되었다면 종료
                break
        elif 0 < n < 1 :    # n에 2를 곱한 값이 0~1 사이라면 ans에 0을 추가
            ans += '0'      # 출력할 답에 0 추가
            cnt += 1        # 소수점 자리 추가

        if cnt == 13:       # 소수점이 12자리를 넘어가면
            ans = 'overflow'
            break

    print(f'#{tc} {ans}')
##################################################################################################################

T = int(input())


def DFS(i, total, lst):
    # DFS 종료조건
    if total > num:  # 1. total이 num보다 크면 유효하지 않음으로 함수 종료
        return 0
    elif total == num:  # 2.total == num이면 lst출력하고 반환값 주기
        for elem in lst:
            print(elem, end='')
        return 1
    if -i > n:  # 3. num이 가지는 소수개수를 다 돌았으면 함수 종료
        return 0

    # DFS 다시 호출하기(반환값 존재 시 함수 종료)
    if DFS(i-1, total+2**i, lst+[1]):  # 2**i를 더하는 경우
        return 1
    if DFS(i-1, total, lst+[0]): # 2**i를 더하지 않는 경우
        return 1


for tc in range(1, T + 1):
    num = input()
    n = len(num[2:])  # n: num의 소수부 개수
    num = float(num)

    print(f'#{tc}', end=' ')
    if not DFS(-1, 0, []):  # num은 소수부를 무조건 가지기 때문에 -1부터 시작
        print('overflow', end=' ')
    print()