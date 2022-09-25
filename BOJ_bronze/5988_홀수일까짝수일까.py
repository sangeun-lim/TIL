n = int(input())
for i in range(n):
    x = input()
    if x[-1] in '02468':
        print('even')
    else:
        print('odd')