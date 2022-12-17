a = int(input())
cnt = 0
if a == 1 :
    print(f'The largest square has side length {a}.')
else:
    for i in range(1,a+1):
        if i ** 2 <= a :
            cnt += 1
        else:
            print(f'The largest square has side length {cnt}.')
            break