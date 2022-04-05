n = int(input())

stack = []
res = []
cnt = 1
tmp = True

for i in range(n):
    num = int(input())  # 수열로 표현할 값 순서대로 입력받기

    while cnt <= num :   # num 이하 숫자는 다 스택에 넣기
        stack.append(cnt)
        res.append('+')
        cnt += 1

    if stack[-1] == num: # 입력들어오는 값이랑, 스택의 마지막값이랑 같을때
        stack.pop()
        res.append('-')
    else :                  # 다를 때
        tmp = False
        break

if tmp == False :       # 수열이 만들어지지 않으면
    print('NO')
else :                  # 수열이 만들어지면
    for i in res:
        print(i)


