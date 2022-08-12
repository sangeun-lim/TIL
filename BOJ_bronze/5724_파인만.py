while True:
    x = int(input())
    if x == 0 :
        break
    total = 0
    for i in range(1,x+1):
        total += i**2

    print(total)