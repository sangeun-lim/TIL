h = int(input())
if h == 0 :
    print(1)
elif h == 1 :
    print(0)
else :
    if h % 2 == 0: # 짝수면
        str = ''
    else:
        str = '4'
    str += '8' * (h // 2)
    print(str)