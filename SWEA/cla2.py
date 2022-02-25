import sys
sys.stdin = open('input.txt')

# for tc in range(1,11):
#     N = int(input())
#     problem = list(map(str,input()))
#     stack = []                   # 괄호와 연산자를 넣을 스택
#     num_oper = []                # 숫자를 넣을 스택

    # 우선순위 지정
    # icp = {'*':2, '+':1, '(':3 } # in-coming priority 넣을때 우선순위
    # isp = {'*':2, '+':1, '(':0 } # in-stack priority 스택안 우선순위

    # 후위 표기식 으로 바꾸기
    # for p in problem:
    #     if p.isdigit():             # 숫자인 경우 스택에 넣기
    #         num_oper.append(p)
    #     else :                      # 연산자나 괄호인 경우
    #         if p == '(' :           # 스택이 비어있을 때 <<< '(' 가 들어오는 경우
    #             stack.append(p)
    #         else :                  # '+' , '*', ')' 가 들어오는 경우
    #             if p == ')':
    #                 while stack[-1] != '(':
    #                     v = stack.pop()
    #                     num_oper.append(v)
    #                 stack.pop()  # '(' 버리기
    #             elif stack and icp[p] > isp[stack[-1]]:       # 들어오는 값의 우선순위가 스택안 우선순위보다 높다면
    #                 stack.append(p)
    #             else:
    #                 while stack and icp[p] <= isp[stack[-1]]:
    #                     v = stack.pop()
    #                     num_oper.append(v)
    #                 stack.append(p)
    # while stack:
    #     num_oper.append(stack.pop())

for tc in range(1,11):
    N = int(input())
    problem = list(map(str,input()))
    stack = []                   # 괄호와 연산자를 넣을 스택
    num_oper = []                # 숫자를 넣을 스택
    # 후위 표기식으로 바꾸기
    for p in problem:
        if p.isdigit():
            num_oper.append(p)
        else :
            if p == '*': # '*'가 들어올때
                stack.append(p)
            else: # '+'가 들어오는 경우
                while stack:
                    num_oper.append(stack.pop())
                stack.append(p)

    while stack:
        num_oper.append(stack.pop())

    # 후위 표기식 계산하기
    number = []  # 피연산자를 쌓을 스택
    for n in num_oper:
        if n.isdigit():
            number.append(n)
        else :
            num1 = int(number.pop())
            num2 = int(number.pop())
            if n == '+':
                num3 = num2 + num1
            else :
                num3 = num2 * num1
            number.append(num3)

    result = number[0]

    print(f'#{tc} {result}')
