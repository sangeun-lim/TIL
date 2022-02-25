import sys
sys.stdin=open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    come = list(map(str,input().split()))       # 피연산자와 연산자가 들어옴
    oper = ['+','-','*','/']
    number = []                                 # 숫자를 저장할 스택
    result = 1                                  # 결과 판단을 위한 result

    for c in come :                             # come 에서 하나씩 꺼내옴
        if c in oper:                           # c가 연산자이면
            num1 = int(number.pop())            # 맨 뒤 값을 꺼내고
            if not number:                      # 하나만 빼냈는데 스택이 비어있으면 error  << 계산할 숫자가 부족한 경우
                result = 0
                break
            num2 = int(number.pop())                 # if문에서 걸리지 않았다면, 다음숫자를 꺼내고
            if c == oper[0] :                   # 각 해당 연산에 맞게 계산 후 append
                num3 = num2+num1
                number.append(num3)
            elif c == oper[1] :
                num3 = num2 - num1
                number.append(num3)
            elif c == oper[2] :
                num3 = num2 * num1
                number.append(num3)
            else :
                num3 = num2//num1     # 나누어떨어진다해도 소수점으로 나올수 있으므로 '//' 사용, 조건에 나눗셈의 경우 항상 나누어 떨어진다고함
                number.append(num3)

        else :                                  # 피연산자이거나 '.' 이면
            if c != '.' :                       # 끝이 아니라면 << 숫자라면
                number.append(c)
            else :                              # '.' 이 들어오면 << 마지막 계산값을 꺼내라는 것을 의미
                if len(number) == 1:            # 스택에 남아있는 게 1개면
                    num4 = number.pop()
                else :                          # 2개 이상인 경우는 연산자가 부족했다는 의미
                    result = 0                  # error

    if result == 1:
        print(f'#{tc} {num4}')
    else :
        print(f'#{tc} error')