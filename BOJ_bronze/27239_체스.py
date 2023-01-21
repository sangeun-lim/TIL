N = int(input())
X = N % 8
if N % 8 == 0 :
    print('h', end='')
    print(N//8)
else:
    print(chr(96+X),end='')
    print(N//8+1)

################################
n = int(input())

print(chr((n-1) % 8 + ord('a')) + str((n-1) // 8 + 1))
