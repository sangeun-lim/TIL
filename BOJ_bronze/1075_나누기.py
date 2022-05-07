N = int(input())
F = int(input())

N = str(N)
a = int(N[:len(N)-2] + '00')

for i in range(a,a+100):
    if i % F == 0 :
        x = str(i)
        print(x[-2:])
        break