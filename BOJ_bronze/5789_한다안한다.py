N = int(input())
for i in range(N):
    x = input()
    if x[len(x)//2-1] == x[len(x)//2]:
        print('Do-it')
    else:
        print('Do-it-Not')