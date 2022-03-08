while True:
    str_list = input()
    if str_list == '.':
        break
    stack = []
    for j in str_list:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            elif not stack or stack[-1] == '[':
                stack.append(j)
                break
        elif j == ']':
            if stack and stack[-1] == '[':
                stack.pop(-1)
            elif not stack or stack[-1] == '(':
                stack.append(j)
                break
    if stack :
        print('no')
    else :
        print('yes')