# 1 = 1
# 2 = 3
# 3 = 7
# 4 = 13
# 5 = 21
# 6 = 31

while True :
    x = int(input())
    if x == 0:
        break
    else :
        print(f'{x} => {x*(x-1)+1}')