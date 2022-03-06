T = int(input())
for tc in range(T):
    gwalho = list(map(str,input()))
    stack = []
    for i in gwalho:
        if not stack:
            stack.append(i)
            if stack[0] == ')':
                break
        elif stack and i == '(':
            stack.append(i)
        elif stack and i == ')':
            stack.pop(-1)

    if not stack:
        print('YES')
    else:
        print('NO')
