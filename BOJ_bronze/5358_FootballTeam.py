while True:
    try:
        x = ''
        y = input()
        for i in y:
            if i == 'i':
                x += 'e'
            elif i == 'e':
                x += 'i'
            elif i == 'I':
                x += 'E'
            elif i == 'E':
                x += 'I'
            else :
                x += i
        print(x)
    except EOFError:
        break

##############################
while True:
    try:
        print(input().replace('i', '"').replace('e', 'i').replace('"', 'e').replace('I', '"').replace('E', 'I').replace('"', 'E'))
    except:
        break
