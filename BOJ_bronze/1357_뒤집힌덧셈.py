x,y = input().split()
x = x[::-1]
y = y[::-1]

z = str(int(x) + int(y))
z = int(z[::-1])

print(z)

####################
x,y = input().split()

def Rev(n):
    return int(str(n)[::-1])

print(Rev(Rev(x) + Rev(y)))