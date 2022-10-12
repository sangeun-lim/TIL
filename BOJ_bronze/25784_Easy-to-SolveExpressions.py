x,y,z = map(int,input().split())
if x + y == z or x + z == y or y + z == x :
    print(1)
elif x * y == z or x * z == y or y * z == x:
    print(2)
else:
    print(3)