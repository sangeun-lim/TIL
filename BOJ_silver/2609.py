a, b = map(int,input().split())

def gcd(x,y):
    while y > 0:
        x , y = y , x % y
    return x
    
def lcm(x,y):
    a = x // gcd(x,y)
    b = y // gcd(x,y)
    
    return a * b * gcd(x,y)
    
print(gcd(a,b))
print(lcm(a,b))