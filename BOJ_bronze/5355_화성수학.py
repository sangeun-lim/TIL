T = int(input())
for tc in range(T):
    total = 0
    arr = list(input().split())
    total = float(arr[0])
    arr.pop(0)
    for i in arr:
        if i == '@':
            total *= 3
        elif i == '%':
            total += 5
        else :
            total -= 7

    print(f'{total:.2f}')