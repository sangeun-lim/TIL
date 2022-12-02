N = int(input())
for i in range(N):
    x = int(input())
    for j in range(x):
        for k in range(x):
            if j == 0 or j == (x-1) or k == 0 or k == (x-1):
                print('#',end='')
            else:
                print('J',end='')
        print()
    print()